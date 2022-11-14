import os
from celery import Celery
from datetime import timedelta

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "price_monitor.settings.production")
app = Celery("price_monitor")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.conf.beat_schedule = {
    'fetch_live_rates_1m':{
        'task': 'sockets.tasks.push_live_rates',
        'schedule': timedelta(minutes=1)
    }
}

app.autodiscover_tasks()


