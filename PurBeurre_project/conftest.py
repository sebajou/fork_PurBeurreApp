import pytest
from django.core.management import call_command
from django.conf import settings


@pytest.fixture(scope='session')
def django_db_setup(django_db_setup, django_db_blocker):
    # settings.DATABASES['default'] = {
    #     'ENGINE': 'django.db.backends.postgresql',
    #     'HOST': 'localhost',
    #     'NAME': 'test_pur_beurre_v6_db',
    #     'USER': 'sebajou',
    #     'PASSWORD': '3333argh',
    #     'PORT': '5432',
    # }
    try:
        with django_db_blocker.unblock():
            call_command('loaddata', 'test1_pur_beurre_v8_db.json', verbosity=1)
        print('conftest for populate test database')
    except:
        print('conftest fail to populate test database')
