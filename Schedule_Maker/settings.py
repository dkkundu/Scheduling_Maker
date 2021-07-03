"""
Django settings for Schedule_Makerproject.

Generated by 'django-admin startproject' using Django 3.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
# PYTHON IMPORTS
import os
# PROJECT IMPORTS
from Schedule_Maker.local_settings import (
    SECRET_KEY, TEMPLATES_DIR, STATICFILES_DIR, STATIC_DIR, MEDIA_DIR,
    LOGS_DIR, DEBUG, ENABLE_HTTPS, ALLOWED_HOSTS, INTERNAL_IPS, DB_CONFIG,
    CELERY_BROKER_URL, CELERY_RESULT_BACKEND, CELERY_CACHE_BACKEND,
    CORS_ALLOWED_ORIGINS
)
from Schedule_Maker.logging import LOGGING
from Schedule_Maker.juzzmin import CONFIG

PROJECT_NAME = 'Schedule_Maker'

# Build paths inside the project like this: os.path.join(BASE_DIR, ...) -------
SETTINGS_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(SETTINGS_DIR)
TEMPLATES_DIR = os.getenv('TEMPLATES_DIR', TEMPLATES_DIR)
STATICFILES_DIR = os.getenv('STATICFILES_DIR', STATICFILES_DIR)
STATIC_DIR = os.getenv('STATIC_DIR', STATIC_DIR)
MEDIA_DIR = os.getenv('MEDIA_DIR', MEDIA_DIR)
LOGS_DIR = os.getenv('LOGS_DIR', LOGS_DIR)


# Quick-start development settings - unsuitable for production ----------------
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = SECRET_KEY  # local_settings.py

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('DEBUG', DEBUG)

# Add domain name, i.e. example.com
ALLOWED_HOSTS = ALLOWED_HOSTS  # local_settings.py

# HTTPS configuration
if ENABLE_HTTPS:  # local_settings
    USE_X_FORWARDED_HOST = True
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True

# needed for debug toolbar
INTERNAL_IPS = INTERNAL_IPS  # local_settings.py

# CORS HEADERS
CORS_ALLOWED_ORIGINS = CORS_ALLOWED_ORIGINS
CORS_ALLOW_ALL_ORIGINS = DEBUG  # Allows from all origins when DEBUG mode is on


# Application definition ------------------------------------------------------

DJANGO_APPS = [
    # https://django-jazzmin.readthedocs.io/
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.humanize',
]

# add 3rd party applications here
PLUGIN_APPS = [
    # https://github.com/korfuri/django-prometheus
    'django_prometheus',
    # https://django-debug-toolbar.readthedocs.io/en/latest/
    'debug_toolbar',
    # https://django-import-export.readthedocs.io/en/stable/index.html
    'import_export',
    # https://github.com/un1t/django-cleanup
    'django_cleanup.apps.CleanupConfig',
    # https://github.com/jazzband/django-widget-tweaks
    'widget_tweaks',
    # https://www.django-rest-framework.org/#installation
    'rest_framework',
    # https://www.django-rest-framework.org/api-guide/authentication/#tokenauthentication
    'rest_framework.authtoken',
    # https://github.com/carltongibson/django-filter
    'django_filters',
    # https://github.com/adamchainz/django-cors-headers
    'corsheaders',
    # https://docs.celeryproject.org/en/stable/django/first-steps-with-django.html#extensions
    'django_celery_results',
    # https://docs.celeryproject.org/en/stable/userguide/periodic-tasks.html
    'django_celery_beat',
    # https://django-dbbackup.readthedocs.io/
    'dbbackup',
    'crispy_forms',
]

# add project applications here
PROJECT_APPS = [
    'Core',
    'API',
    'drop_calendar.apps.DropCalendarConfig',
]

# consolidate all installed applications here
INSTALLED_APPS = DJANGO_APPS + PLUGIN_APPS + PROJECT_APPS

SITE_ID = 1  # Sites framework

MIDDLEWARE = [
    'django_prometheus.middleware.PrometheusBeforeMiddleware',  # prometheus
    'debug_toolbar.middleware.DebugToolbarMiddleware',  # debug_toolbar
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',  # corsheaders
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_prometheus.middleware.PrometheusAfterMiddleware',  # prometheus
]

ROOT_URLCONF = 'Schedule_Maker.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR, ],
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

# https://docs.djangoproject.com/en/3.2/releases/3.2/#customizing-type-of-auto-created-primary-keys
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'  # suppress model warning

WSGI_APPLICATION = 'Schedule_Maker.wsgi.application'

AUTH_USER_MODEL = 'Core.User'

LOGIN_URL = '/auth/login/'
LOGIN_REDIRECT_URL = 'index'
LOGOUT_REDIRECT_URL = 'index'

CRISPY_TEMPLATE_PACK = 'bootstrap4'


# Database --------------------------------------------------------------------
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': os.getenv('DB_CONFIG', DB_CONFIG)
}


# Password validation ---------------------------------------------------------
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.'
                'UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.'
                'MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.'
                'CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.'
                'NumericPasswordValidator',
    },
]


# Django REST Framework -------------------------------------------------------
# https://www.django-rest-framework.org/api-guide/settings/

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication'
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated'
    ],
    'DEFAULT_FILTER_BACKENDS': [
        # django-filters
        # https://www.django-rest-framework.org/api-guide/filtering/
        # https://django-filter.readthedocs.io/en/latest/guide/rest_framework.html
        'django_filters.rest_framework.DjangoFilterBackend',
        # https://www.django-rest-framework.org/api-guide/filtering/#searchfilter
        'rest_framework.filters.SearchFilter',
        # https://www.django-rest-framework.org/api-guide/filtering/#orderingfilter
        'rest_framework.filters.OrderingFilter'
    ]
}


# Internationalization --------------------------------------------------------
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Dhaka'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images) --------------------------------------
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = STATIC_DIR  # production, don't forget to run collectstatic
STATICFILES_DIRS = [STATICFILES_DIR, ]  # development environment

MEDIA_URL = '/media/'
MEDIA_ROOT = MEDIA_DIR


# Admin panel configuration ---------------------------------------------------
# https://github.com/farridav/django-jazzmin
# https://django-jazzmin.readthedocs.io/
JAZZMIN_SETTINGS = CONFIG

ADMIN_URL = 'manage'  # do not include any leading/trailing slashes


# Logging ---------------------------------------------------------------------
# https://docs.djangoproject.com/en/3.2/topics/logging/

if os.getenv('DISABLE_LOGGING', False):  # for celery in jenkins ci only
    LOGGING_CONFIG = None
LOGGING = LOGGING  # logging.py


# Email -----------------------------------------------------------------------
# https://docs.djangoproject.com/en/3.0/topics/email/

try:  # optional settings import
    from Schedule_Maker.local_settings import EMAIL_BACKEND
    EMAIL_BACKEND = EMAIL_BACKEND
except ImportError:  # use default if not defined in local_settings
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'


# Celery ----------------------------------------------------------------------
# https://docs.celeryproject.org/en/stable/userguide/configuration.html#configuration-and-defaults
CELERY_BROKER_URL = os.getenv(
    'CELERY_BROKER_URL', CELERY_BROKER_URL
)

# https://docs.celeryproject.org/en/stable/django/first-steps-with-django.html#extensions
CELERY_RESULT_BACKEND = os.getenv(
    'CELERY_RESULT_BACKEND', CELERY_RESULT_BACKEND
)
CELERY_CACHE_BACKEND = os.getenv(
    'CELERY_CACHE_BACKEND', CELERY_CACHE_BACKEND
)


# DbBackup --------------------------------------------------------------------
# https://django-dbbackup.readthedocs.io/

# AWS S3 EXAMPLE
# https://django-dbbackup.readthedocs.io/en/master/storage.html#amazon-s3
# DBBACKUP_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
# DBBACKUP_STORAGE_OPTIONS = {
#     'access_key': AWS_ACCESS_KEY_ID,
#     'secret_key': AWS_SECRET_ACCESS_KEY,
#     'bucket_name': AWS_STORAGE_BUCKET_NAME,
#     'default_acl': 'private',
#     'location': 'backup/',
# }

DBBACKUP_STORAGE = 'django.core.files.storage.FileSystemStorage'
DBBACKUP_STORAGE_OPTIONS = {'location': 'backup/'}
