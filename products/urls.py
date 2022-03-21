from django.urls import path

import products.views

urlpatterns = [
    path(
        '<str:product_searched>/',
        products.views.products,
        name='products'
    ),
    path(
        'detail/<str:product>/',
        products.views.product_details,
        name='product_details'
    ),
    path(
        'substitute/<str:product>/',
        products.views.substitute,
        name='substitute'
    ),
]