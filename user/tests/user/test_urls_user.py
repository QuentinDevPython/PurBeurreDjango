import pytest

from django.urls import reverse, resolve


class TestUrlsUser:
    
    @pytest.mark.django_db
    def test_login_url(self):

        path = reverse('login')
        assert path == "/user/"
        assert resolve(path).view_name == "login"

    @pytest.mark.django_db
    def test_logout_url(self):

        path = reverse('logout')
        assert path == "/user/logout/"
        assert resolve(path).view_name == "logout"
        
    @pytest.mark.django_db
    def test_signup_url(self):

        path = reverse('signup')
        assert path == "/user/signup/"
        assert resolve(path).view_name == "signup"