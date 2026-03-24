import requests
import uuid
import json


from django.http import HttpResponseBadRequest, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.core.exceptions import ValidationError
from django.contrib.auth import login, get_user_model

from .model import Listing, ListingStatus


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
        data = json.loads(request.body)
        listing = Listing.objects.create(
            seller=request.user,
            title=data['title'],
            description=data.get('description', ''),
            price_cents=int(data['price_cents']),
            condition=data['condition']
        )
        return JsonResponse({'status': 'success', 'id': listing.id}, status=201)

    # Modify item
    elif request.method == 'PATCH':
        listing = get_object_or_404(Listing, pk=listing_id, seller=request.user)
        data = json.loads(request.body)

        # Allow only when item is active
        if listing.status != ListingStatus.ACTIVE:
            return JsonResponse({'error': 'Cannot modify an inactive item'}, status=400)

        listing.title = data.get('title', listing.title)
        listing.description = data.get('description', listing.description)
        listing.save()
        return JsonResponse({'status': 'updated'})

    # Delete item
    elif request.method == 'DELETE':
        listing = get_object_or_404(Listing, pk=listing_id, seller=request.user)
        listing.status = ListingStatus.REMOVED
        listing.save()
        return JsonResponse({'status': 'deleted'})


def post_bid(request, listing_id):
    if request.method == 'POST':
        listing = get_object_or_404(Listing, pk=listing_id)
        data = json.loads(request.body)
        try:
            amount = int(data['amount_cents'])
            bid = listing.place_bid(request.user, amount)
            return JsonResponse({
                'status': 'success',
                'new_price': listing.price_cents,
                'bid_id': bid.id
            })
        except (ValidationError, ValueError) as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

#
# Render Frontend
#
def index(request):
    return render(request, 'index.html')