import pytest

from django.urls import reverse, resolve


@pytest.mark.django_db
def test_login_url():

    path = reverse('login')
    assert path == "/user/"
    assert resolve(path).view_name == "login"

@pytest.mark.django_db
def test_logout_url():

    path = reverse('logout')
    assert path == "/user/logout/"
    assert resolve(path).view_name == "logout"
    
@pytest.mark.django_db
def test_signup_url():

    path = reverse('signup')
    assert path == "/user/signup/"
    assert resolve(path).view_name == "signup"