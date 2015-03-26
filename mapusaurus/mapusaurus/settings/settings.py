"""
Django settings for mapusaurus project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import sys
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '($2ob)%vv$wv7jl-$e!=#z!+bhihs@o%$+@c0yqrz&8*f@#hhi'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
#         'LOCATION': '/var/tmp/django_cache',
#         'TIMEOUT': None,
#     }
# }
# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
#         'LOCATION': '127.0.0.1:11211',
#     }
# }

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',
    'django.contrib.humanize',
    'localflavor',
    'haystack',
    'rest_framework',
    'basestyle',
    'mapping',
    'respondents',
    'geo',
    'censusdata',
    'hmda',
    'api',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
)

STATIC_ROOT = '/var/www/static/'

ROOT_URLCONF = 'mapusaurus.urls'

WSGI_APPLICATION = 'mapusaurus.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases
#DATABASES = {'default': {'ENGINE': '', 'NAME': '', 'USER': '', 'PASSWORD': ''}}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/
STATIC_URL = '/static/'

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
        'URL': 'http://127.0.0.1:9200/',
        'INDEX_NAME': 'mapusaurus',
    },
}

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.TemplateHTMLRenderer',
        'rest_framework.renderers.JSONRenderer',
    ],
}
PDFREACTOR = {
    'HOST': 'localhost',
    'PORT': 9423,
    'KEY': '<license><licenseserialno>3815</licenseserialno><licensee><name>Consumer Financial Protection Bureau</name><address><street>1700 G ST NWSTE 6013-W</street><city>Washington DC</city><country>United States</country></address></licensee><product>PDFreactor</product><majorversion>7</majorversion><minorversion>0</minorversion><licensetype>CPU</licensetype><amount>8</amount><unit>CPU</unit><maintenanceexpirationdate>2016-02-25</maintenanceexpirationdate><expirationdate>2016-02-25</expirationdate><purchasedate>2015-03-26</purchasedate><outputformats><pdf/><image/></outputformats><advanced><conditions><condition>This license is for use on development systems only. It may not be used on staging or productive systems of any kind.</condition></conditions></advanced><signatureinformation><signdate>2015-03-26 16:16</signdate><signature>302d02142ec8a294410005767cb5e0da44c28a0cd9ab35c002150093d18474c9e449770ba73e04d6ed2f8fcc6e7bf2</signature><checksum>3583</checksum></signatureinformation></license>',
}

SOUTH_TESTS_MIGRATE = False

from mapusaurus.settings.local_settings import *
