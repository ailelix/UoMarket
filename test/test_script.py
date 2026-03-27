import os, sys, django
from pydantic import BaseModel
sys.path.append('.')
from src import config

app_conf = config.AppConfig.load_config("config.yaml")

from django.conf import settings
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
settings.configure(
    DEBUG=True,
    SECRET_KEY=app_conf.server.django_secret,
    AUTH_USER_MODEL='src.User',
    DATABASES={
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': app_conf.database.dbname,
            'USER': app_conf.database.username,
            'PASSWORD': app_conf.database.password,
            'HOST': app_conf.database.server,
            'PORT': app_conf.database.port,
        }
    },
    INSTALLED_APPS=['django.contrib.auth', 'django.contrib.contenttypes', 'django.contrib.sessions', 'src'],
    USE_TZ=True,
    TIME_ZONE='Europe/London'
)
django.setup()

from src.models import User, Listing, Category, ListingStatus
from django.utils import timezone
import datetime

user1, _ = User.objects.get_or_create(username='seller')
user2, _ = User.objects.get_or_create(username='buyer')

listing = Listing.objects.create(
    seller=user1,
    title='Test Item',
    price_cents=1000,
    condition='good',
    is_auction=True,
    endtime=timezone.now() + datetime.timedelta(days=1),
    status=ListingStatus.ACTIVE
)

try:
    listing.place_bid(user2, 1500)
    print("BID SUCCESS")
except Exception as e:
    print(f"BID FAILED: {repr(e)}")

# clean up
listing.delete()
