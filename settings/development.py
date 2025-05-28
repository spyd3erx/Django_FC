from .base import *

INSTALLED_APPS.append("debug_toolbar.apps.DebugToolbarConfig")
MIDDLEWARE.append("debug_toolbar.middleware.DebugToolbarMiddleware")

DEBUG = True

ALLOWED_HOSTS.append("*")
# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '3dshop',
        'USER': 'root',
        'PASSWORD': 'mysecretpassword',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}

INTERNAL_IPS = [
    "127.0.0.1"
]

STATICFILES_DIRS = [BASE_DIR / 'static']
MEDIA_ROOT = BASE_DIR / 'media'