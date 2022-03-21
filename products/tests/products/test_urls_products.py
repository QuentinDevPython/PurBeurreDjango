import pytest

from django.urls import reverse, resolve

from products.models import Product


@pytest.mark.django_db
def test_home_url():

    path = reverse('home')
    assert path == "/home/"
    assert resolve(path).view_name == "home"
    
@pytest.mark.django_db
def test_products_url():
    
    product_searched = 'cacao nesquik'
    
    path = reverse(
        'products',
        kwargs={
            'product_searched': product_searched
        }
    )
    
    assert path == "/products/cacao%20nesquik/"
    assert resolve(path).view_name == "products"

@pytest.mark.django_db
def test_product_details_url():
    
    product = Product.objects.create(
        product_name_fr = 'Formule boost',
        countries = 'France',
        stores = 'simply market,intermarché, carrefour.fr',
        grade = 'A',
        url = 'https://fr.openfoodfacts.org/produit/3270720001596/formule-boost-daco-bello',
        image_url = 'https://images.openfoodfacts.org/images/products/327/072/000/1596/front_fr.78.400.jpg',
        conservation_conditions_fr = '',
        additives_original_tags = '',
        allergens_from_ingredients = 'en:soybeans, soja, amandes',
        ingredients_text_fr = 'Cranberries (cranberries séchées, sucre, huile de tournesol), graines de _soja_ grillées, _amandes_ torréfiées, graines de courge grillées,'
    )
    
    path = reverse(
        'product_details',
        kwargs={
            'product': product
        }
    )
    
    assert path == "/products/detail/Formule%20boost/"
    assert resolve(path).view_name == "product_details"
    
@pytest.mark.django_db
def test_substitute_url():
    
    product = Product.objects.create(
        product_name_fr = 'Formule boost',
        countries = 'France',
        stores = 'simply market,intermarché, carrefour.fr',
        grade = 'A',
        url = 'https://fr.openfoodfacts.org/produit/3270720001596/formule-boost-daco-bello',
        image_url = 'https://images.openfoodfacts.org/images/products/327/072/000/1596/front_fr.78.400.jpg',
        conservation_conditions_fr = '',
        additives_original_tags = '',
        allergens_from_ingredients = 'en:soybeans, soja, amandes',
        ingredients_text_fr = 'Cranberries (cranberries séchées, sucre, huile de tournesol), graines de _soja_ grillées, _amandes_ torréfiées, graines de courge grillées,'
    )
    
    path = reverse(
        'substitute',
        kwargs={
            'product': product
        }
    )
    
    assert path == "/products/substitute/Formule%20boost/"
    assert resolve(path).view_name == "substitute"
    