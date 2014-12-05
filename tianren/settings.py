"""
Django settings for tianren project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '42b88&72$ird_i+3u+eci@h%+rw(&1e5gc#krhvy#k9pmz%#x8'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sites',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'tianren.datamodel',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)
SITE_ID = 1

ROOT_URLCONF = 'tianren.urls'

WSGI_APPLICATION = 'tianren.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    # }
    'default' : {
        'ENGINE'    : 'django.db.backends.mysql',
        'NAME'      : 'c9',
        'USER'      : 'arlinajsk',
        'HOST'      : '127.0.0.1',
        'PORT'      : '3306',
    }    
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

#TIME_ZONE = 'UTC'
TIME_ZONE = 'US/Eastern'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

# DATABASES = {
#     'default' : {
#         'ENGINE'    : 'django.db.backends.mysql',
#         'NAME'      : 'tianrenDB',
#         'USER'      : 'admin2hHtUuu',
#         'PASSWORD'  : 'a7aL3KyzvQwr',
#         'HOST'      : '127.4.125.130',
#         'PORT'      : '3306',
#     }
# }


# howto
# http://support.cloud9ide.com/entries/21285626-How-do-I-push-my-Cloud9-project-to-GitHub

# TEMPLATE_DIRS = {
#     'tianren/templates',
    
# }
TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates'), 'tianren/templates']