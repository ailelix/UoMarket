import requests
import uuid
import json


from django.http import HttpResponseBadRequest, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.core.exceptions import ValidationError
from django.contrib.auth import login, get_user_model
from django.db.models import Q
from django.db import transaction
from django.core.files.storage import FileSystemStorage

from .models import Listing, ListingStatus, Category, ListingImage

User = get_user_model()

UOM_AUTH_BASE = "http://studentnet.cs.manchester.ac.uk/authenticate/"


#
# UoM login
#
def uom_login_start(request):
    # Generate the unique ticket
    cs_ticket = uuid.uuid4().hex
    request.session['cs_ticket'] = cs_ticket

    callback_url = request.build_absolute_uri('/api/callback')

    # Redirect to UoM
    uom_auth_url = (
        f"{UOM_AUTH_BASE}?"
        f"url={callback_url}&csticket={cs_ticket}&version=3&command=validate"
    )
    return redirect(uom_auth_url)

def uom_auth_callback(request):
    # Get parameters back
    username = request.GET.get('username')
    fullname = request.GET.get('fullname')
    ticket_res = request.GET.get('csticket')
    ticket_session = request.session.pop('cs_ticket', None) # Fetch and delete1. 生成并存储唯一的 CSTICKET

    # Verify ticket
    if not ticket_session or ticket_res != ticket_session:
        return HttpResponseBadRequest('Invalid or expired session ticket')

    # Send confirmation to UoM
    callback_url = request.build_absolute_uri('/api/callback')
    confirm_url = (
        f"{UOM_AUTH_BASE}?"
        f"url={callback_url}&csticket={ticket_session}"
        f"&version=3&command=confirm&username={username}&fullname={fullname}"
    )

    try:
        response = requests.get(confirm_url, timeout=10)
        # Verify confirmation response
        if response.status_code == 200:
            user, created = User.objects.get_or_create(
                username=username,
                defaults={"first_name": fullname}
            )
            from .models import UserStatus
            if user.status == UserStatus.SUSPENDED or not user.is_active:
                return HttpResponseBadRequest('Your account has been suspended')
            login(request, user)
            return redirect('/')
        else:
            return HttpResponseBadRequest('Auth confirmation failed at server')
    except requests.RequestException:
        return HttpResponseBadRequest('Connection to auth server failed')


#
# APIs
#
def manage_listing(request, listing_id=None):
    # Create item
    if request.method == 'POST':
        # Data is now expected as multipart/form-data, not JSON
        data = request.POST
        files = request.FILES

        if 'image' not in files:
            return JsonResponse({'error': 'An image is required for a new listing.'}, status=400)

        try:
            with transaction.atomic():
                is_auction = data.get('is_auction') == 'true'
                parsed_endtime = None
                if is_auction and data.get('endtime'):
                    from django.utils.dateparse import parse_datetime
                    from django.utils import timezone
                    parsed_endtime = parse_datetime(data['endtime'])
                    if parsed_endtime and parsed_endtime <= timezone.now():
                        return JsonResponse({'error': 'Auction end time must be in the future'}, status=400)

                listing = Listing.objects.create(
                    seller=request.user,
                    title=data['title'],
                    description=data.get('description', ''),
                    price_cents=int(data['price_cents']),
                    condition=data['condition'],
                    is_auction=is_auction,
                    endtime=parsed_endtime
                )
                
                ListingImage.objects.create(listing=listing, image=files['image'])

                # Handle categories, assuming they are sent as multiple form fields with the same name
                categories_names = data.getlist('categories')
                if categories_names:
                    cat_list = []
                    for cat_name in categories_names:
                        cat_name = str(cat_name).strip()
                        if cat_name:
                            cat_obj, _ = Category.objects.get_or_create(name=cat_name)
                            cat_list.append(cat_obj)
                    listing.categories.set(cat_list)


            return JsonResponse({'status': 'success', 'id': listing.id}, status=201)
        except KeyError as e:
            return JsonResponse({'error': f'Missing required field: {e}'}, status=400)
        except Exception as e:
            return JsonResponse({'error': 'An unexpected error occurred while creating the listing.'}, status=500)

    # Modify item
    elif request.method == 'PATCH':
        if listing_id is None:
            return JsonResponse({'error': 'Listing ID required'}, status=400)
        listing = get_object_or_404(Listing, pk=listing_id, seller=request.user)
        data = json.loads(request.body)

        # Allow only when item is active or reserved
        if listing.status not in [ListingStatus.ACTIVE, ListingStatus.RESERVED]:
            return JsonResponse({'error': 'Cannot modify a sold or removed item'}, status=400)

        listing.title = data.get('title', listing.title)
        listing.description = data.get('description', listing.description)
        if 'price_cents' in data:
            listing.price_cents = int(data['price_cents'])
        if 'condition' in data:
            listing.condition = data['condition']
        
        if 'status' in data:
            valid_statuses = [choice[0] for choice in ListingStatus.choices]
            if data['status'] in valid_statuses:
                listing.status = data['status']
                
        if not listing.is_auction:
            if 'is_auction' in data:
                listing.is_auction = data['is_auction']
            if 'endtime' in data:
                from django.utils.dateparse import parse_datetime
                from django.utils import timezone
                parsed_time = parse_datetime(data['endtime']) if data['endtime'] else None
                if parsed_time and parsed_time <= timezone.now():
                    return JsonResponse({'error': 'Auction end time must be in the future'}, status=400)
                listing.endtime = parsed_time
        
        listing.save()
        if 'categories' in data and data['categories'] is not None:
            cat_list = []
            for cat_name in data['categories']:
                cat_name = str(cat_name).strip()
                if cat_name:
                    cat_obj, _ = Category.objects.get_or_create(name=cat_name)
                    cat_list.append(cat_obj)
            listing.categories.set(cat_list)
            
        return JsonResponse({'status': 'updated'})

    # Delete item
    elif request.method == 'DELETE':
        if listing_id is None:
            return JsonResponse({'error': 'Listing ID required'}, status=400)
        listing = get_object_or_404(Listing, pk=listing_id, seller=request.user)
        listing.status = ListingStatus.REMOVED
        listing.save()
        return JsonResponse({'status': 'deleted'})


def post_bid(request, listing_id=None):
    if request.method == 'POST':
        data = json.loads(request.body)
        l_id = listing_id or data.get('itemId')
        listing = get_object_or_404(Listing, pk=l_id)
        try:
            amount = int(data.get('amount_cents') or data.get('amount'))
            bid = listing.place_bid(request.user, amount)
            return JsonResponse({
                'status': 'success',
                'new_price': listing.price_cents,
                'bid_id': bid.id
            })
        except (ValidationError, ValueError) as e:
            msg = e.messages[0] if hasattr(e, 'messages') and e.messages else str(e)
            return JsonResponse({'status': 'error', 'message': msg}, status=400)

def _settle_expired_auctions():
    from django.utils import timezone
    from .models import Order, OrderStatus
    now = timezone.now()
    expired = Listing.objects.filter(
        is_auction=True, 
        endtime__lte=now, 
        status=ListingStatus.ACTIVE
    )
    for item in expired:
        highest_bid = item.bids.first()
        if highest_bid:
            item.status = ListingStatus.SOLD
            Order.objects.create(
                listing=item,
                buyer=highest_bid.user,
                seller=item.seller,
                amount_cents=highest_bid.amount_cents,
                status=OrderStatus.PLACED
            )
        else:
            item.status = ListingStatus.REMOVED
        item.save()

def get_items(request):
    _settle_expired_auctions()
    if request.method == 'GET':
        keyword = request.GET.get('keyword')
        category_name = request.GET.get('category')
        seller_id = request.GET.get('seller')
        sort_by = request.GET.get('sort') # createtime/endtime/name/price
        order = request.GET.get('order', 'asc') # asc/desc
        is_open = request.GET.get('open') # false/true
        
        qs = Listing.objects.all()
        
        if keyword:
            qs = qs.filter(Q(title__icontains=keyword) | Q(description__icontains=keyword))
            
        if category_name:
            qs = qs.filter(categories__name__iexact=category_name)
            
        if seller_id:
            qs = qs.filter(seller_id=seller_id)
            
        if is_open == 'true':
            qs = qs.filter(status=ListingStatus.ACTIVE)
        elif is_open == 'false':
            qs = qs.exclude(status=ListingStatus.ACTIVE)
            
        if sort_by:
            prefix = '-' if order == 'desc' else ''
            sort_map = {
                'createtime': 'created_at',
                'endtime': 'endtime',
                'name': 'title',
                'price': 'price_cents'
            }
            if sort_by in sort_map:
                qs = qs.order_by(prefix + sort_map[sort_by])
                
        results = []
        for item in qs:
            first_image = item.images.first()
            results.append({
                "id": item.id,
                "name": item.title,
                "image": first_image.image.url if first_image else None,
                "price_cents": item.price_cents
            })
        return JsonResponse(results, safe=False)

def handle_items_api(request):
    if request.method == 'GET':
        return get_items(request)
    elif request.method in ['POST', 'PATCH', 'DELETE']:
        return manage_listing(request)
    return JsonResponse({'error': 'Method not allowed'}, status=405)

def handle_single_item_api(request, item_id):
    if request.method == 'GET':
        return get_item(request, item_id)
    elif request.method in ['PATCH', 'DELETE']:
        return manage_listing(request, listing_id=item_id)
    return JsonResponse({'error': 'Method not allowed'}, status=405)

def get_item(request, item_id):
    _settle_expired_auctions()
    if request.method == 'GET':
        item = get_object_or_404(Listing, pk=item_id)
        categories = list(item.categories.values_list('name', flat=True))
        
        highest_bid = item.bids.first()
        bid_amount = highest_bid.amount_cents if highest_bid else item.price_cents
        
        images = [img.image.url for img in item.images.all()]
        
        data = {
            "id": item.id,
            "name": item.title,
            "description": item.description,
            "condition": item.condition,
            "categories": categories,
            "image": images[0] if images else None,
            "images": images,
            "auction": "auction" if item.is_auction else "sale",
            "status": item.status,
            "bid": bid_amount,
            "ddl": item.endtime.isoformat() if item.endtime else None,
            "seller_id": item.seller.id
        }
        return JsonResponse(data)

def get_user(request, user_id):
    if request.method == 'GET':
        user = get_object_or_404(User, pk=user_id)
        items = list(user.listings.values_list('id', flat=True))
        return JsonResponse({
            "name": user.full_name or user.username,
            "items": items
        })

def get_category(request, category_id):
    if request.method == 'GET':
        category = get_object_or_404(Category, pk=category_id)
        return JsonResponse({
            "name": category.name
        })
        
def get_categories(request):
    if request.method == 'GET':
        cats = list(Category.objects.values('id', 'name'))
        return JsonResponse(cats, safe=False)

from django.views.decorators.csrf import ensure_csrf_cookie

#
# User Session APIs
#
@ensure_csrf_cookie
def get_me(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return JsonResponse({
                "id": request.user.id,
                "username": request.user.username,
                "name": getattr(request.user, 'first_name', '') or getattr(request.user, 'full_name', '') or request.user.username,
                "email": request.user.email
            })
        return JsonResponse({"error": "Not authenticated"}, status=401)

def uom_logout(request):
    from django.contrib.auth import logout
    if request.method == 'POST':
        logout(request)
        return JsonResponse({"status": "success"})


#
# Render Frontend
#
@ensure_csrf_cookie
def index(request):
    return render(request, 'index.html')