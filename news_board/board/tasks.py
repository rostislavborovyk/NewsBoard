from __future__ import absolute_import, unicode_literals

from celery.task import periodic_task
from celery.schedules import crontab

from .models import Post


# task executes daily ad midnight
@periodic_task(run_every=(crontab(minute=0, hour=0)), name="reset_upvotes")
def reset_upvotes():
    for post in Post.objects.all():
        post.amount_of_upvotes = 0
        post.save()
