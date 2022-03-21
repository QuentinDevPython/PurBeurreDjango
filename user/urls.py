from django.urls import path

import user.views

from django.contrib.auth.views import LoginView


urlpatterns = [
    path(
        '',
        LoginView.as_view(
            template_name='user/login.html',
            redirect_authenticated_user=True
        ),
        name='login'
    ),
    path(
        'logout/',
        user.views.logout_user,
        name='logout'
    ),
    path(
        'signup/',
        user.views.signup_page,
        name='signup'
    ),
]