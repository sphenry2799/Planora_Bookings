import os
from pathlib import Path

# -------------------
# BASE DIR
# -------------------
BASE_DIR = Path(__file__).resolve().parent.parent

# -------------------
# SECRET KEY
# -------------------
SECRET_KEY = os.environ.get("SECRET_KEY")
if not SECRET_KEY:
    raise ValueError("SECRET_KEY not set in environment variables!")

# -------------------
# DEBUG
# -------------------
DEBUG = os.environ.get("DEBUG", "False") == "True"

# -------------------
# ALLOWED HOSTS
# -------------------
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
    'django.contrib.sites',

    # django-allauth
    'allauth',
    'allauth.account',
    'allauth.socialaccount',

    # your apps
    'reservations',
    'django_summernote',
    'about',
]

# -------------------
# Sites framework
# -------------------
SITE_ID = 1

# -------------------
# MIDDLEWARE
# -------------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # for static files on Heroku
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# -------------------
# ROOT URL
# ------------------
