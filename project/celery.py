# project/celery.py

import os
from celery import Celery
from celery.schedules import crontab

from django.conf import settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
app = Celery("project")
app.conf.enable_utc = False
app.conf.update(timezone=settings.CELERY_TIMEZONE)
app.conf.beat_schedule = {
    
}
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f"\rRequest: {self.request!r}")
    