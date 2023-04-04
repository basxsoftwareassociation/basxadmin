import os

from celery import Celery

# DJANGO_SETTINGS_MODULE environment variable must be set before this module is imported
# We set this to production if not already set

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "basxadmin.settings.production")
app = Celery("basxadmin")

# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object("django.conf:settings", namespace="CELERY")

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()
