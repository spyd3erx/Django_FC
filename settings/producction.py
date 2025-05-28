from .base import *

DEBUG = False

ALLOWED_HOSTS.append("")

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "OPTIONS": {
            "read_default_file": "database/my.cnf",
        },
    }
}
STATIC_ROOT = BASE_DIR / 'staticfiles'
MEDIA_ROOT = BASE_DIR / 'media'

# Recopilar los archivos statics
# py manage.py collectstatic