import os
from pathlib import Path
import dj_database_url

# Base directory
BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')

# -------------------
# SECRET KEY
# -------------------
SECRET_KEY = os.environ.get("SECRET_KEY")  

# -------------------
# DEBUG
# -------------------
DEBUG = False

# -------------------
# ALLOWED HOSTS
# -------------------
if DEBUG:
    ALLOWED_HOSTS = ['localhost', '127.0.0.1']
else:
    ALLOWED_HOSTS = ['planora-reservations-32b582e35d5e.herokuapp.com']

# -------------------
# INSTALLED APPS
# -------------------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'reservations',  # your app
]

# -------------------
# MIDDLEWARE
# -------------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # if using whitenoise
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',  # must be here
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# -------------------
# ROOT URLS
# -------------------
ROOT_URLCONF = 'planorabookings.urls'

# -------------------
# TEMPLATES
# -------------------
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],   # <-- this is correct
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

# -------------------
# WSGI
# -------------------
WSGI_APPLICATION = 'planorabookings.wsgi.application'

# -------------------
# DATABASE
# -------------------
DATABASES = {
    'default': dj_database_url.parse(
        os.environ.get('DATABASE_URL', f"sqlite:///{BASE_DIR / 'db.sqlite3'}")
    )
}

# -------------------
# PASSWORD VALIDATION
# -------------------
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

# -------------------
# INTERNATIONALIZATION
# -------------------
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# -------------------
# STATIC FILES
# -------------------
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# -------------------
# DEFAULT AUTO FIELD
# -------------------
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
