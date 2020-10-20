from django.test import Client
import pytest
from database_handler_app.views import my_foods
from database_handler_app.models import MyUsers


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
        self.search_food_request = {'items': 'beurre de cacahuète'}
        self.user_bilbo_to_login = {'username': 'Bilbo', 'password': '3 anneaux pour les lier tous'}

    def test_index(self):
        response = c.get('/')
        assert response.status_code == 200

    def test_legal_mention(self):
        response = c.get('/database_handler_app/legal_mention/')
        assert response.status_code == 200

    def test_my_foods(self):
        response = c.get('/database_handler_app/my_foods/')
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_route_user_form(self):
        user_data_to_post = self.user_to_post
        response = c.post('/user_form/', user_data_to_post)
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_route_user_login(self):
        user_data_to_login = self.user_to_login
        response = c.post('/accounts/login/', user_data_to_login)
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_search_food(self):
        search_food_req = self.search_food_request
        response = c.post('/database_handler_app/search_results/', search_food_req)
        assert response.status_code == 200

    def test_route_user_profile(self):
        response_profile = c.get('/accounts/profile/')
        assert response_profile.status_code == 200

    def test_route_logout(self):
        response_profile = c.get('/accounts/logout/')
        assert response_profile.status_code == 200

    def test_route_password_reset(self):
        response_profile = c.get('/accounts/password_reset/')
        assert response_profile.status_code == 200

