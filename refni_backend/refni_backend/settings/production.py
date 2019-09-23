# Production settings. Settings must be safe.
from refni_backend.refni_backend.settings.base import *


DEBUG = False

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

DB_SERVER_ADDRESS = '127.0.0.1'
CELERY_BROKER_ADDRESS = 'amqp://localhost'

# TODO: FILL THESE IN AFTER SETTING UP PRODUCTION ENV
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'refni_db',
        'OPTIONS': {
            'sql_mode': 'STRICT_TRANS_TABLES',
        },
        'HOST': DB_SERVER_ADDRESS,
        'PORT': '3306',
        'USER': '',
        'PASSWORD': '',
    }
}

# FULL PATH to the folder where you store uploaded files
MEDIA_ROOT = os.path.join(BASE_DIR, 'uploaded_files')

# Debug only. DO NOT USE ALLOW_ALL in production.
CORS_ORIGIN_ALLOW_ALL = False

# TODO: Limit user submission, say 10 submissions per day
