"""
Django settings for kyd_finance project.

Generated by 'django-admin startproject' using Django 5.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
from django.utils.translation import gettext_lazy as _
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()



# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY =  os.getenv('SECRET_KEY')



ALLOWED_HOSTS = ['*']


# Application definition
# setting up installed apps

INSTALLED_APPS = [

     # DJANGO INTERNAL APPS
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Django apps generated
    'accounts.apps.AccountsConfig',
    'main.apps.MainConfig',
    'blog.apps.BlogConfig',


    # THIRD PARTY APPS
    'rosetta',
    'parler',
    'phonenumber_field',
    'social_django',
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',

    # Adding the middleware for internalization
    'django.middleware.locale.LocaleMiddleware',  

    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'kyd_finance.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['template/'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'kyd_finance.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

USE_I18N = True

# Enable localization
USE_L10N = True

# adding the language code
LANGUAGES = [
     ('en', _('English')),
    ('es', _('Spanish')),
    ('fr', _('French')),
]

# adding locale path
LOCALE_PATHS = [BASE_DIR / 'locale',]

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# setting up django parler for translating models
PARLER_LANGUAGES = {
    None:(
        {'code' : 'en'},
        {'code' : 'es'},
        {'code': 'fr'},
    ),
    'default': {
        'fallbacks': ['en'],
        'hide_untranslated': False,
        },
        }

# aDDING MEDIA URL

MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR/'media'


DEBUG = True



# setting upthe url

LOGIN_REDIRECT_URL = 'dashboard'
LOGIN_URL = 'login'
LOGOUT_URL = 'logout'

# adding email backend
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# Email Configuration
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')


# setting up authentication backend
AUTHENTICATION_BACKENDS =  [
 'django.contrib.auth.backends.ModelBackend',
 'social_core.backends.google.GoogleOAuth2',
]

# setting the google oauth
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = os.getenv('GOOGLE_OAUTH2_KEY')
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = os.getenv('GOOGLE_OAUTH2_SECRET')

# setting up socialpipeline
SOCIAL_AUTH_PIPELINE = [
 'social_core.pipeline.social_auth.social_details',
 'social_core.pipeline.social_auth.social_uid',
 'social_core.pipeline.social_auth.auth_allowed',
 'social_core.pipeline.social_auth.social_user',
 'social_core.pipeline.user.get_username',
  'social_core.pipeline.user.create_user',
   'account.authentication.create_profile',
 'social_core.pipeline.social_auth.associate_user',
 'social_core.pipeline.social_auth.load_extra_data',
 'social_core.pipeline.user.user_details',
]

