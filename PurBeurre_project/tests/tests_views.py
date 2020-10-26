from django.test import Client
from django.contrib.sessions.models import Session
from django import urls
# from django.urls import reverse
# from database_handler_app.models import MyUsers
import pytest
# import freezegun
# import datetime as dt
# from django.test.testcases import SimpleTestCase

c = Client()


class TestRoutesGeneral:
    """Test index and homes pages routes """

    def setup_method(self):
        self.search_food_request = {'items': 'beurre de cacahuète'}

    def test_index(self):
        response = c.get('/')
        assert response.status_code == 200

    def test_legal_mention(self):
        response = c.get('/database_handler_app/legal_mention/')
        assert response.status_code == 200

    def test_my_foods(self):
        response = c.get('/database_handler_app/my_foods/')
        assert response.status_code == 200

    def test_search_food(self):
        search_food_req = self.search_food_request
        response = c.post('/database_handler_app/search_results/', search_food_req)
        assert response.status_code == 200


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
        # There should be a user with 'my_username'
        # user = MyUsers.objects.get(username='LeGrandMechantLoup')
        # The user's last login time should be set to the current time
        # assert user.last_login == dt.datetime(2019, 1, 26, 7)

    @pytest.mark.django_db
    def test_route_user_login(self):
        user_data_to_login = self.user_to_login
        response = c.post('/accounts/login/', user_data_to_login, follow=True)
        assert response.status_code == 200
        # The login view should redirect us to profile page
        # SimpleTestCase().assertRedirects(response, reverse('profile'))
        # assert response.status_code == 302
        # assert response.url == urls.reverse('profile')

    def test_route_user_profile(self):
        response_profile = c.get('/accounts/profile/')
        assert response_profile.status_code == 200

    @pytest.mark.django_db
    def test_route_logout(self):
        response_profile = c.get('/accounts/logout/')
        assert response_profile.status_code == 200
        # There should be no more sessions left after logging out
        assert not Session.objects.exists()

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

