import os
import sys

POSTGRES_HOST = 'localhost'
if os.getenv('DOCKER_CONTAINER'):
    POSTGRES_HOST = 'db'


if 'test' in sys.argv:
    DATABASES['default'] = {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'test_djaein',
        'USER': 'djaein',
        'PASSWORD': 'djaein',
        'HOST': POSTGRES_HOST,
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'djaein',
            'USER': 'djaein',
            'PASSWORD': 'djaein',
            'HOST': POSTGRES_HOST,
            'PORT': '5432',
        }
    }
TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
NOSE_ARGS = [
    '--with-coverage',
    '--cover-package=users,personal',
    '--cover-html',
    '--cover-erase'
]

ALLOWED_HOSTS = ['*']
