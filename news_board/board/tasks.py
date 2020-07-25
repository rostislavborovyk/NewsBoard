from __future__ import absolute_import, unicode_literals

from celery.task import periodic_task
from celery.schedules import crontab

from .models import Post


# task executes daily ad midnight
@periodic_task(run_every=(crontab(minute=0, hour=0)), name="reset_upvotes")
def reset_upvotes():
    """Task resets upvotes for every post to 0"""
    for post in Post.objects.all():
        post.amount_of_upvotes = 0
        post.save()


# task executes every minute
@periodic_task(run_every=(crontab(minute="*/1")), name="debug")
def debug():
    """Task for checking whether cron tasks work"""
    print("Task debug message")
