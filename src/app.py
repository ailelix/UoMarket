import sys
import django
from django.conf import settings
from django.core.management import execute_from_command_line
from .middleware import AuthMiddleware


def run(app_conf):
    # Setup Django
    if not settings.configured:
        settings.configure(
            DEBUG=True,
            SECRET_KEY=app_conf.server.django_secret,
            # Pass config from config.yaml
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
            INSTALLED_APPS=[
                'django.contrib.auth',
                'django.contrib.contenttypes',
                'django.contrib.sessions',
                'src',
            ],
            MIDDLEWARE=[
                'django.contrib.sessions.middleware.SessionMiddleware',
                'django.middleware.common.CommonMiddleware',
                'django.middleware.csrf.CsrfViewMiddleware',
                'django.contrib.auth.middleware.AuthenticationMiddleware',
                'src.middleware.AuthMiddleware', # Custom middleware
            ],
            ROOT_URLCONF='src.route',
            TIME_ZONE='Europe/London',
            USE_TZ=True,
        )
        django.setup()

    # Prepare booting parameters
    # Pass host and port to the startup command
    addrport = f"{app_conf.server.host}:{app_conf.server.port}"
    sys.argv = ['manage.py', 'runserver', addrport, '--nothreading', '--noreload']

    execute_from_command_line(sys.argv)