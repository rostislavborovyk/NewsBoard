import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'news_board.settings')

app = Celery("news_board")
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()
