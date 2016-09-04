

from datetime import timedelta

CELERYBEAT_SCHEDULE = {
    'add-every-30-seconds': {
        'task': 'laundry.update',
        'schedule': timedelta(seconds=30),
    },
}

CELERY_TIMEZONE = 'UTC'




