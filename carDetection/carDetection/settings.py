"""
Django settings for carDetection project.

Generated by 'django-admin startproject' using Django 5.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
from key import github_cid, github_csecrets, google_cid, google_csecrets
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-zqrgn4d+n#!+&ruqp**58xvyq3=o$@hmb#m=f$ug@4%s$g6m&!"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "location_field.apps.DefaultConfig",
    "django.contrib.sites",  # social
    "allauth",  # social
    "allauth.account",  # socail
    "allauth.socialaccount",  # social
    "allauth.socialaccount.providers.github",  # github
    "allauth.socialaccount.providers.google",  # google
     'allauth.socialaccount.providers.facebook', # facebook
    "phonenumber_field",
    "django_celery_results",
    "process",
    "user",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "allauth.account.middleware.AccountMiddleware",  # social
]

ROOT_URLCONF = "carDetection.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "carDetection.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    # Postgres
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "postgres",
        "USER": "postgres",
        "PASSWORD": "postgres",
        "HOST": "db",
        "PORT": 5432,
    },
    # # SQLite
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': BASE_DIR / 'db.sqlite3',
    # }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

AUTH_USER_MODEL = "user.Profile"


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Asia/Bangkok"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = "static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Celery Configuration
CELERY_BROKER_URL = "amqp://celery:celery1234@localhost:5672/myvhost"
CELERY_RESULT_BACKEND = "django-db"
CELERY_CACHE_BACKEND = "django-cache"
CELERY_BROKER_TRANSPORT_OPTIONS = {
    "data_folder_in": os.path.join(BASE_DIR, "celery", "queue"),
    "data_folder_out": os.path.join(BASE_DIR, "celery", "queue"),
    "data_folder_processed": os.path.join(BASE_DIR, "celery", "processed"),
}

# social
AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",  # social
    "allauth.account.auth_backends.AuthenticationBackend",  # social
]

SITE_ID = 1  # social
ACCOUNT_EMAIL_VERIFICATION = "none"
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = False
LOGIN_REDIRECT_URL = "/"
SOCIALACCOUNT_LOGIN_ON_GET = True
ACCOUNT_LOGOUT_ON_GET = True


# social
SOCIALACCOUNT_PROVIDERS = {
    "github": {
        "carDetection": {
            "client_id": github_cid,
            "secret": github_csecrets,
        },
        "SCOPE": [
            "user",
            "repo",
            "read:org",
        ],
    },
    "google": {
        "Django CarDetection": {
            "client_id": google_cid,
            "secret": google_csecrets,
            "key": "",
        }
    },
    'facebook': {
        'METHOD': 'oauth2',
        'SDK_URL': '//connect.facebook.net/{locale}/sdk.js',
        'SCOPE': ['email', 'public_profile'],
        'AUTH_PARAMS': {'auth_type': 'reauthenticate'},
        'INIT_PARAMS': {'cookie': True},
        'FIELDS': [
            'id',
            'email',
            'first_name',
            'last_name',
            'middle_name',
            'name',
            'name_format',
            'picture',
            'short_name'
        ],
        'EXCHANGE_TOKEN': True,
        'LOCALE_FUNC': lambda request: 'en_US',
        'VERIFIED_EMAIL': False,
        'VERSION': 'v7.0',
    },
}

LOCATION_FIELD = {
    "map.provider": "openstreetmap",
    "provider.openstreetmap.max_zoom": 18,
}
