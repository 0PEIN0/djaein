from django.conf import settings

from core import DataLoader
from django_celery_beat.models import IntervalSchedule, PeriodicTask

if User.objects.filter(email=settings.APPLICATION_SYS_ADMIN_EMAIL).exists() is False:
    User.objects.create_superuser(
        email=settings.APPLICATION_SYS_ADMIN_EMAIL,
        password=settings.APPLICATION_SYS_ADMIN_PASSWORD)

sys_user = User.objects.get(email=settings.APPLICATION_SYS_ADMIN_EMAIL)

model_initial_data_schema = [
    {
        'model': IntervalSchedule,
        'data': [
            {
                'every': 5,
                'period': 'seconds'
            },
            {
                'every': 10,
                'period': 'seconds'
            },
            {
                'every': 30,
                'period': 'seconds'
            },
            {
                'every': 60,
                'period': 'seconds'
            },
            {
                'every': 120,
                'period': 'seconds'
            },
            {
                'every': 300,
                'period': 'seconds'
            },
        ]
    },
    {
        'model': PeriodicTask,
        'data': [
            {
                'name': 'mark_old_to_do_as_done',
                'task': 'personal.tasks.mark_old_to_do_as_done',
                'enabled': True
            },
        ]
    },
]


data_list = DataLoader().insert_initial_data(
    schema=model_initial_data_schema)

print('INITAL DATA LOAD COMPLETE')
