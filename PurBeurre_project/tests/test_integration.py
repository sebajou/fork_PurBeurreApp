from django.http import HttpResponse
from django.test import Client
from django.contrib.sessions.models import Session
from django import urls
import pytest
import time
from request_api_app.search_engine import PopDBFromJsonWithCategories, FindSubstitute, Parser
from request_api_app.search_engine import pop_db_with_categories
import json
from schema import Schema, And
from database_handler_app.models import FoodList, Allergen
import ast
from bs4 import BeautifulSoup
from django.urls import reverse


c = Client()

@pytest.fixture
def test_password():
    return 'strong-test-pass'


@pytest.fixture
def create_user(db, django_user_model, test_password):
    """User mock. """
    def make_user(**kwargs):
        kwargs['password'] = "1AQWXSZ2"
        if 'username' not in kwargs:
            kwargs['username'] = "LeGrandMechantLoup"
        if 'id' not in kwargs:
            kwargs['id'] = 1
        return django_user_model.objects.create_user(**kwargs)
    return make_user


class TestIntegration:

    def setup_method(self):
        self.search_food_request = {'search': 'beurre de cacahuète'}
        self.user_to_login = {'username': 'cornebouque', 'password': '1AQWXSZ2'}
        self.food_id = {'items': 662}
        self.favorite_id = {'favorite_substitute_id': 662}

    @pytest.mark.django_db
    def test_signup_logout(self, client, create_user):
        user = create_user()
        client.login(
            username=user.username, password="1AQWXSZ2"
        )
        response = client.get('http://127.0.0.1:8000/accounts/logout/')
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_login_search_add_favorite(self, client, create_user, django_user_model):
        # mock request.user
        user = django_user_model.objects.create(
            username='someone', password='password'
        )
        url = reverse('user-detail-view', kwargs={'pk': user.pk})
        response = client.get(url)

        # Create user and connect
        user = create_user()
        client.login(
            username=user.username, password="1AQWXSZ2"
        )
        # Search food
        search_food_request = {'search': 'beurre de cacahuète'}
        response = c.post('/database_handler_app/search_results/', search_food_request)
        # Extract id from html in response.content
        soup = BeautifulSoup(response.content, features="html.parser")
        print("soup => ", soup)
        find_id = soup.find(id='favorite_substitute_id_0')
        print("find_id => ", find_id)
        first_id_from_search = int(find_id['value'])
        print("first_id_from_search => ", first_id_from_search)
        response = c.post('/database_handler_app/is_favorite/',
                          {'username': 'cornebouque', 'favorite_substitute_id': first_id_from_search})
        assert response.status_code == 302

    @pytest.mark.django_db
    def test_login_serch_display_page_food(self):
        pass
