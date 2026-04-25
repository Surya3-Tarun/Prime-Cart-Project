import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = 'django-insecure-primecart-secret-key'

DEBUG = True

ALLOWED_HOSTS = []


INSTALLED_APPS = [

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',   # Required for Google Login

    # Project Apps
    'products',
    'cart',
    'orders',
    'payments',
    'reviews',
    'users',
    'wishlist',
    'coupons',

    # Authentication (Google Login)
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',

]


MIDDLEWARE = [

    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'allauth.account.middleware.AccountMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',


]


ROOT_URLCONF = 'primecart.urls'


TEMPLATES = [
{
'BACKEND': 'django.template.backends.django.DjangoTemplates',
'DIRS': [BASE_DIR / 'templates'],
'APP_DIRS': True,
'OPTIONS': {
'context_processors': [

'django.template.context_processors.debug',
'django.template.context_processors.request',
'django.contrib.auth.context_processors.auth',
'django.contrib.messages.context_processors.messages',

'cart.views.cart_count',
'wishlist.views.wishlist_count',

],
},
},
]


WSGI_APPLICATION = 'primecart.wsgi.application'


DATABASES = {
'default': {
'ENGINE': 'django.db.backends.sqlite3',
'NAME': BASE_DIR / 'db.sqlite3',
}
}


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


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_TZ = True


# Static files
STATIC_URL = '/static/'

STATICFILES_DIRS = [
BASE_DIR / "static",
]


# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Google Authentication Settings
SITE_ID = 1

AUTHENTICATION_BACKENDS = [

'django.contrib.auth.backends.ModelBackend',

'allauth.account.auth_backends.AuthenticationBackend',

]


LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'