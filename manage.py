import sys
import os

from src import app
from src import config

if __name__ == "__main__":
    app_conf = config.AppConfig.load_config("config.yaml")

    import django
    from django.conf import settings

    if not settings.configured:
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
            TEMPLATES=[{
                'BACKEND': 'django.template.backends.django.DjangoTemplates',
                'DIRS': [os.path.join(os.path.dirname(os.path.abspath(__file__)), 'frontend', 'dist')],
                'APP_DIRS': True,
            }],
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
                'src.middleware.AuthMiddleware',
            ],
            ROOT_URLCONF='src.route',
            TIME_ZONE='Europe/London',
            USE_TZ=True,
        )
        django.setup()

    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
