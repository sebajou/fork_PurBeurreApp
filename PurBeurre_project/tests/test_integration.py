from django.test import Client
import pytest
from bs4 import BeautifulSoup


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


@pytest.fixture
def auto_login_user(db, client, create_user, test_password):
    def make_auto_login(user=None):
        if user is None:
            user = create_user()
        client.login(username=user.username, password=test_password)
        return client, user
    return make_auto_login


@pytest.mark.django_db
def test_login_search_add_favorite(auto_login_user):
    # mock request.user and login
    client, user = auto_login_user()
    response = client.post('/accounts/login/', {'username': 'LeGrandMechantLoup', 'password': '1AQWXSZ2'})
    # Search food
    search_food_request = {'search': 'beurre de cacahuète'}
    response = client.post('/database_handler_app/search_results/', search_food_request)
    # Extract id from html in response.content
    soup = BeautifulSoup(response.content, features="html.parser")
    find_id = soup.find(id='favorite_substitute_id_0')
    first_id_from_search = int(find_id['value'])
    response = client.post('/database_handler_app/is_favorite/', {'favorite_substitute_id': first_id_from_search})
    assert response.status_code == 302


@pytest.mark.django_db
def test_signup_logout(client, create_user):
    user = create_user()
    client.login(
        username=user.username, password="1AQWXSZ2"
    )
    response = client.get('http://127.0.0.1:8000/accounts/logout/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_login_search_display_page_food(auto_login_user):
    # mock request.user and login
    client, user = auto_login_user()
    response = client.post('/accounts/login/', {'username': 'LeGrandMechantLoup', 'password': '1AQWXSZ2'})
    # Search food
    search_food_request = {'search': 'beurre de cacahuète'}
    response = client.post('/database_handler_app/search_results/', search_food_request)
    # Extract id from html in response.content
    soup = BeautifulSoup(response.content, features="html.parser")
    find_id = soup.find(id='favorite_substitute_id_0')
    first_id_from_search = int(find_id['value'])
    # Display page food
    response = client.post('/database_handler_app/food_page/', {'id_food': first_id_from_search})
    assert response.status_code == 200
