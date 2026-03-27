from django.contrib.auth.models import AbstractUser
from django.db import models, transaction
from django.conf import settings
from django.core.exceptions import ValidationError

# Enum Definition
class UserStatus(models.TextChoices):
    PENDING = "pending_verification", "Pending Verification"
    VERIFIED = "verified", "Verified"
    SUSPENDED = "suspended", "Suspended"

class ListingCondition(models.TextChoices):
    NEW = "new", "New"
    LIKE_NEW = "like_new", "Like New"
    GOOD = "good", "Good"
    FAIR = "fair", "Fair"
    POOR = "poor", "Poor"

class ListingStatus(models.TextChoices):
    ACTIVE = "active", "Active"
    RESERVED = "reserved", "Reserved"
    SOLD = "sold", "Sold"
    REMOVED = "removed", "Removed"

class OrderStatus(models.TextChoices):
    PLACED = "placed", "Placed"
    PAID = "paid", "Paid"
    CANCELLED = "cancelled", "Cancelled"
    REFUNDED = "refunded", "Refunded"
    COMPLETED = "completed", "Completed"

class OrderEventType(models.TextChoices):
    CREATED = "created", "Created"
    PAID = "paid", "Paid"
    CANCELLED = "cancelled", "Cancelled"
    COMPLETED = "completed", "Completed"
    REFUNDED = "refunded", "Refunded"
    MESSAGE = "message", "Message"

# Model Definition
class User(AbstractUser):
    """
    Custom user model for Django
    """
    full_name = models.CharField(max_length=255)
    status = models.CharField(
        max_length=30,
        choices=UserStatus.choices,
        default=UserStatus.PENDING
    )
    last_login_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'users'

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        db_table = 'categories'
        verbose_name_plural = "Categories"

class Listing(models.Model):
    seller = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='listings')
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    price_cents = models.PositiveIntegerField()
    condition = models.CharField(max_length=20, choices=ListingCondition.choices)
    status = models.CharField(max_length=20, choices=ListingStatus.choices, default=ListingStatus.ACTIVE)
    categories = models.ManyToManyField(Category, related_name='listings')
    is_auction = models.BooleanField(default=False)
    endtime = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def place_bid(self, user, amount_cents):
        """
        Process new bids
        """
        from django.utils import timezone
        
        # Verification
        if self.status != ListingStatus.ACTIVE:
            raise ValidationError("The item is not active")
        if self.is_auction and self.endtime and self.endtime <= timezone.now():
            raise ValidationError("The auction has already ended")
        if user == self.seller:
            raise ValidationError("You cannot bid your own item")
        if amount_cents <= self.price_cents:
            raise ValidationError("The new price must be higher than the current")

        # Atomic transaction
        with transaction.atomic():
            # select_for_update locks this row
            listing = Listing.objects.select_for_update().get(pk=self.pk)

            # Check price again
            if amount_cents <= listing.price_cents:
                raise ValidationError("Someone else has put a higher bid")

            # Update price
            listing.price_cents = amount_cents
            listing.save()

            # Create bid record
            return Bid.objects.create(listing=listing, user=user, amount_cents=amount_cents)

class Bid(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='bids')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    amount_cents = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-amount_cents'] # Higher price in front

class ListingImage(models.Model):
    listing = models.ForeignKey(
        Listing,
        on_delete=models.CASCADE,
        related_name='images'
    )
    image = models.ImageField(upload_to='listing_images/', null=True, blank=True)
    sort_order = models.IntegerField(default=0)

    class Meta:
        db_table = 'listing_images'

class Order(models.Model):
    listing = models.OneToOneField(
        Listing,
        on_delete=models.PROTECT,
        related_name='order'
    )
    buyer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name='orders_bought'
    )
    seller = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name='orders_sold'
    )
    amount_cents = models.PositiveIntegerField()
    status = models.CharField(
        max_length=20,
        choices=OrderStatus.choices,
        default=OrderStatus.PLACED
    )
    created_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'orders'

class OrderEvent(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name='events'
    )
    event_type = models.CharField(max_length=50)
    event_data = models.JSONField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True
    )

    class Meta:
        db_table = 'order_events'