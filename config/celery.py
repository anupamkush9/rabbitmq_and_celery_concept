import os
from celery import Celery
# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
app = Celery('config')
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')
# With the below line Celery will automatically discover tasks from all of your installed apps, following the tasks.py convention.
app.autodiscover_tasks()