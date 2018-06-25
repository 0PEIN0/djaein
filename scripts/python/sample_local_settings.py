import sys

if 'test' in sys.argv:
    DATABASES['default'] = {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'test_djaein',
        'USER': 'djaein',
        'PASSWORD': 'djaein',
        'HOST': 'localhost',
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'djaein',
            'USER': 'djaein',
            'PASSWORD': 'djaein',
            'HOST': 'localhost',
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
