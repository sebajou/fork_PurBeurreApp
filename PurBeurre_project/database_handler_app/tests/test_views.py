from PurBeurre_project.database_handler_app import views as database_handler_views
from django.test import TestCase
from django.test import Client

"""
@pytest.fixture
def client():
    database_handler_views.config['TESTING'] = True

    with database_handler_views.test_client() as client:
        yield c"""

c = Client()
# Test of different routes


class TestRoutes:

    def setup_method(self):
        self.user_to_post = {'username': 'frodobessac', 'first_name': 'Frodon', 'last_name': 'Sacquet',
                             'email': 'frodon.sacquet@gmail.com', 'diet_type': ' omnivore',
                             'alergy': ['amande', 'banane', 'kiwi'], 'password1': '1AQWXSZ2', 'password2': '1AQWXSZ2'}
        self.user_to_login = {'username': 'LeGrandMechantLoup', 'password': '1AQWXSZ2'}


    def test_test(self):
        a = 3
        b = 3
        assert a == b

    def test_route_user_form(self):
        user_data_to_post = self.user_to_post
        response = c.post('/user_form/', user_data_to_post)
        assert response.status_code == 200

    def test_route_user_login(self):
        user_data_to_login = self.user_to_login
        response = c.post('/login/', user_data_to_login)
        assert response.status_code == 200
