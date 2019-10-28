# Any dev settings can be placed here
from refni_backend.refni_backend.settings.base import *


DEBUG = True

ALLOWED_HOSTS = []

# DB_SERVER_ADDRESS = '127.0.0.1'
DB_SERVER_ADDRESS = 'mongodb+srv://refni-ugp06.mongodb.net/test'
CELERY_BROKER_ADDRESS = 'amqp://127.0.0.1'

DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'refni',
        'HOST': DB_SERVER_ADDRESS,
        'USER': 'ClouDroid',
        'PASSWORD': 'WeAreAllOnThe4thFloor'
    }
}

# FULL PATH to the folder where you store uploaded files (WE'RE NOT SAVING FILES LOCALLY!)
MEDIA_ROOT = os.path.join(BASE_DIR, 'uploaded_files')

# Default file storage engine
# DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

# Debug only. DO NOT USE ALLOW_ALL in production.
CORS_ORIGIN_ALLOW_ALL = True
