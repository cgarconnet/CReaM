# coding: utf8
"""
Django settings for cream project.

Generated by 'django-admin startproject' using Django 1.8.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MAIN_DIR = os.path.dirname(os.path.dirname(__file__))

ON_HEROKU = os.environ.get('ON_HEROKU')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'q2u+id*ao8j^)(!*y&dlrd4fa%%s$#*0h!ic6vs3*q%o*5(vhl'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',
    'widget_tweaks', # for managing the forms easier
    'sitegate', # to enable the sign-in
    'bootstrap3', # required by sitegate
    'geoposition', # for google maps
    'bootstrap_pagination', # for the pagination of our list    
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'cream.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(MAIN_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.contrib.auth.context_processors.auth',
                'django.core.context_processors.debug',
                'django.core.context_processors.i18n',
                'django.core.context_processors.media',
                'django.core.context_processors.static',
                'django.core.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
                'django.core.context_processors.request',
            ],
        },
    },
]

WSGI_APPLICATION = 'cream.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

# Chris - now we check if we are on Heroku
if ON_HEROKU == '1':

    # Parse database configuration from $DATABASE_URL
    import dj_database_url
#    DATABASES['default'] = dj_database_url.config()
    DATABASES = {'default' : dj_database_url.config()}


else: 
    # else we use local sqlite database
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = '/static/' # Pour le deploiement sur Heroku

LOGIN_URL = '/entrance'

STATICFILES_DIRS = (
    os.path.join(MAIN_DIR, 'static'),
    )

# Lines below should be activated for Amazon Web Services
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
AWS_S3_FORCE_HTTP_URL = True
AWS_QUERYSTRING_AUTH = False
AWS_SECRET_ACCESS_KEY = os.environ.get('AWSSecretKey')
AWS_ACCESS_KEY_ID = os.environ.get('AWSAccessKeyId')
AWS_STORAGE_BUCKET_NAME = 'onemonthpythongarconnet'

