from django.urls import path

import favorites.views

urlpatterns = [
    path(
        'my_food/<str:product>/',
        favorites.views.my_food,
        name='my_food'
    ),
]