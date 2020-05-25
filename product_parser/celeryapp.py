from __future__ import absolute_import, unicode_literals
import os
import django
# from celery import Celery
django.setup()
from product_parser.loads import load_celery
from product_parser.services.tasks_service import TasksService


# set the default Django settings module for the 'celery' program.

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Crawler.settings')

# app = Celery('products')
os.environ[ 'DJANGO_SETTINGS_MODULE' ] = "Crawler.settings"

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# namespace='CELERY' means all celery-related configuration keys
# should have a `CELERY_` prefix.
# app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
# app.autodiscover_tasks()

app = load_celery()
celery_task = app.task

tasks = TasksService()


@celery_task()
def parse_pages():
    tasks.parse_page()
