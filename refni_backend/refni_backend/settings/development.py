# Any dev settings can be placed here
from refni_backend.refni_backend.settings.base import *


DEBUG = True

ALLOWED_HOSTS = []

DB_SERVER_ADDRESS = '127.0.0.1'
CELERY_BROKER_ADDRESS = 'amqp://127.0.0.1'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'refni_db.sqlite3',
    }
}

# FULL PATH to the folder where you store uploaded files
MEDIA_ROOT = os.path.join(BASE_DIR, 'uploaded_files')

# Debug only. DO NOT USE ALLOW_ALL in production.
CORS_ORIGIN_ALLOW_ALL = True
