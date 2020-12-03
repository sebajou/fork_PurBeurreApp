import pytest
from django.core.management import call_command


@pytest.fixture(scope='session')
def django_db_setup(django_db_setup, django_db_blocker):
    print('conftest for populate test database')
    with django_db_blocker.unblock():
        call_command('loaddata', 'test_pur_beurre_v5_db.json')
