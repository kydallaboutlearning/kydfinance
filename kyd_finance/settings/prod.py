from .base import *
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# setting up debug mode

DEBUG = False


# setting up the allowed hosts
ALLOWED_HOSTS = ['127.0.0.1', 'localhost','hot-lola-kyd-45e60a62.koyeb.app']


STORAGES = {
    # ...
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST'),
        'OPTIONS': {'sslmode': 'require'},
    }
}


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}


SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
SECURE_SSL_REDIRECT = True


CKEDITOR_UPLOAD_PATH = "uploads/"
DEFAULT_FILE_STORAGE = "django.core.files.storage.FileSystemStorage"
