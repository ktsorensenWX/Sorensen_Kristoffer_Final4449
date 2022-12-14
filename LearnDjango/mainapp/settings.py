"""
Django settings for aimdb project.

Generated by 'django-admin startproject' using Django 3.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import keras
import numpy as np
import tensorflow.keras.backend as K
import tensorflow as tf
from tensorflow.python.keras.backend import set_session
from keras.applications import vgg16

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'pr75j7t*r!j=oac!798tazlecdo0%k0rasre@!f_&0u%2(=nty'
import os, sys

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*', 'localhost']

AUTO_LOGOUT_DELAY=30000
# Application definition

ACCOUNT_AUTHENTICATION_METHOD="username_email"

ACCOUNT_EMAIL_VERIFICATION = "none"
ACCOUNT_USERNAME_REQUIRED=False
ACCOUNT_ACTIVATION_DAYS = 7 # One-week activation window
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS=0
ACCOUNT_EMAIL_REQUIRED = False
ACCOUNT_LOGIN_ATTEMPTS_TIMEOUT=86400000000
#ACCOUNT_EMAIL_VERIFICATION = "mandatory"
ACCOUNT_SESSION_REMEMBER = True
ACCOUNT_USERNAME_MIN_LENGTH = 3
ACCOUNT_EMAIL_SUBJECT_PREFIX="Hello: "

AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend'
]

CRISPY_TEMPLATE_PACK="bootstrap4"
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sites',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #'corsheaders',
    'allauth',
    'allauth.account',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.github',

    #My apps
    'mainapp',
    'app1',
    'app2',
 ];

SITE_ID = 1

# Provider specific settings
DEFAULT_AUTO_FIELD='django.db.models.BigAutoField'
CORS_ORIGIN_ALLOW_ALL = True   

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mainapp.urls'
#---------------------------------------------------------------------------------
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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
WSGI_APPLICATION = 'mainapp.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

AUTH_PASSWORD_VALIDATORS = [
#    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
#    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
#    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
#    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
]

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
SESSION_SAVE_EVERY_REQUEST = True

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N  = True
USE_L10N  = True
USE_TZ    = True

STATIC_URL = '/static/'
STATICFILES_DIRS = ( os.path.join(BASE_DIR, 'static'), "/")
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
