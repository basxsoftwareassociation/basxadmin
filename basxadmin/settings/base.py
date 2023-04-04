# flake8: noqa
"""
For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

import os

from basxbread.settings.required import *

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(PROJECT_DIR)

SECRET_KEY = "django-insecure-l_0)wu)-ttk_n-o-5x#r3#wla71_wonof5*(*u+1y-h39q-p9#"

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    # custom apps
    "django.contrib.admin",
    "basxconnect.core",
    "basxconnect.invoicing",
    "basxconnect.projects",
    "basxbread.contrib.document_templates",
] + BASXBREAD_DEPENDENCIES

ROOT_URLCONF = "basxadmin.urls"

WSGI_APPLICATION = "wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}

HAYSTACK_CONNECTIONS = {
    "default": {
        "ENGINE": "haystack.backends.whoosh_backend.WhooshEngine",
        "PATH": os.path.join(BASE_DIR, "woosh_index"),
    },
}

STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATIC_URL = "/static/"

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"

TEMPLATES[0]["OPTIONS"]["context_processors"].append(
    "basxconnect.core.context_processors.basxconnect_core"
)
