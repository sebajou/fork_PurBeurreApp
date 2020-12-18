from django.test import Client
import pytest

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


class TestRoutesGeneral:
    """Test index and homes pages routes """

    def setup_method(self):
        self.search_food_request = {'items': 'beurre de cacahuète'}
        self.user_to_login = {'username': 'LeGrandMechantLoup', 'password': '1AQWXSZ2'}
        self.food_id = {'items': 662}
        self.favorite_id = {'favorite_substitute_id': 662}

    def test_index(self):
        response = c.get('/')
        assert response.status_code == 200

    def test_request_api_app(self):
        response = c.get('/request_api_app/')
        assert response.status_code == 200

    def test_legal_mention(self):
        response = c.get('/database_handler_app/legal_mention/')
        assert response.status_code == 200

    def test_my_foods(self):
        response = c.get('/database_handler_app/my_foods/')
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_search_food(self):
        search_food_req = self.search_food_request
        response = c.post('/database_handler_app/search_results/', search_food_req)
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_food_page(self):
        food_page_request = self.food_id
        response = c.post('/database_handler_app/food_page/', food_page_request)
        assert response.status_code == 200
        # assert b'Nous avons une page pour cette aliments. ' in response.content

    @pytest.mark.django_db
    def test_my_foods(self, create_user):
        user = create_user()
        c.login(
            username=user.username, password="1AQWXSZ2"
        )
        response = c.get('/database_handler_app/my_foods/')
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_is_favorite(self, client, create_user):
        user = create_user()
        client.login(
            username=user.username, password="1AQWXSZ2"
        )
        id_food = self.favorite_id
        response = client.post('/database_handler_app/is_favorite/', id_food)
        assert response.status_code == 302


class TestRoutesUsers:
    """Test routes for users session"""

    def setup_method(self):
        self.user_to_post = {'username': 'frodobessac', 'first_name': 'Frodon', 'last_name': 'Sacquet',
                             'email': 'frodon.sacquet@gmail.com', 'diet_type': ' omnivore',
                             'alergy': ['amande', 'banane', 'kiwi'], 'password1': '1AQWXSZ2', 'password2': '1AQWXSZ2'}
        self.user_to_login = {'username': 'LeGrandMechantLoup', 'password': '1AQWXSZ2'}
        self.user_bilbo_to_login = {'username': 'Bilbo', 'password': '3 anneaux pour les lier tous'}
        self.fake_user_to_login = {'username': 'TomBombabile', 'password': '1AQWXSZ2'}

    # @freezegun.freeze_time('2019-01-26 7:00:00')
    @pytest.mark.django_db
    def test_route_user_form(self):
        user_data_to_post = self.user_to_post
        response = c.post('/user_form/', user_data_to_post)
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_route_user_login(self):
        user_data_to_login = self.user_to_login
        response = c.post('/accounts/login/', user_data_to_login, follow=True)
        assert response.status_code == 200

    def test_route_user_profile(self):
        response_profile = c.get('/accounts/profile/')
        assert response_profile.status_code == 200

    @pytest.mark.django_db
    def test_route_logout(self):
        response_profile = c.get('/accounts/logout/')
        assert response_profile.status_code == 200

    def test_route_password_reset(self):
        response_profile = c.get('/accounts/password_reset/')
        assert response_profile.status_code == 200

    @pytest.mark.django_db
    def test_route_fake_user_login(self):
        fake_user = self.fake_user_to_login
        response = c.post('/accounts/login/', fake_user)
        assert response.status_code == 200
        # Verify is display a error message when login fail.
        assert b'Votre nom d\'utilisateur et votre mot de passe ne correspondent pas. Veuillez reessayer.' \
               in response.content
