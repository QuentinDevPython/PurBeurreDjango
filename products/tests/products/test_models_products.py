import pytest

from django.test import Client
from products.models import Product, Category, ProductWithCategory


@pytest.mark.django_db  
def test_product_model():

    client = Client()

    product = Product.objects.create(
        product_name_fr = 'Ricore original, café & chicorée, boîte 100g',
        countries = 'Belgique,France,Espagne,Suisse',
        stores = 'magasins u,al campo (auchan),carrefour,auchan,delhaize, carrefour.fr',
        grade = 'A',
        url = 'https://fr.openfoodfacts.org/produit/3033710073467/ricore-original-cafe-chicoree-boite-100g-nestle',
        image_url = 'https://images.openfoodfacts.org/images/products/303/371/007/3467/front_fr.230.400.jpg',
        conservation_conditions_fr = 'A conserver dans un endroit frais et sec.',
        additives_original_tags = '',
        allergens_from_ingredients = '',
        ingredients_text_fr = 'café soluble 33,2%, fibres de chicorée (oligofructose) 33%, chicorée soluble 30%, sulfate de magnésium,'
    )

    expected_value = "Ricore original, café & chicorée, boîte 100g"
    
    assert str(product) == expected_value

@pytest.mark.django_db  
def test_category_model():

    client = Client()

    category = Category.objects.create(
        category = 'Chocolat-au-lait-aux-morceaux-de-biscuits'
    )
    
    expected_value = "Chocolat-au-lait-aux-morceaux-de-biscuits"
    
    assert str(category) == expected_value

@pytest.mark.django_db  
def test_product_with_category_model():

    client = Client()
    
    product = Product.objects.create(
        product_name_fr = 'Bouillon légumes knorr',
        countries = 'France',
        stores = 'intermarché, carrefour.fr',
        grade = 'A',
        url = 'https://fr.openfoodfacts.org/produit/8712566432127/bouillon-legumes-knorr',
        image_url = 'https://images.openfoodfacts.org/images/products/871/256/643/2127/front_fr.73.400.jpg',
        conservation_conditions_fr = 'À conserver dans un endroit sec et propre après utilisation.',
        additives_original_tags = '',
        allergens_from_ingredients = 'en:celery, CÉLERI, CÉLERI',
        ingredients_text_fr = 'Sel, maltodextrine, graisse de palme, sucre, oignon\': 4%, extrait de levure, CÉLERI-RAVE\': 3,4%, arômes, carotte\': 2,2%, ail\', poireau\':0,6%, curcuma\', graines de fenugrec, livèche\', jus de CELERİ concentré&quot;\', persil\', jus d\'oignon concentré\', poivre, jus de carotte concentré\' : 0,1%, jus de poireau concentré&quot;, huile de tournesol. Peut contenir: gluten, lait, moutarde, ceuf, soja. \'Ingrédients issus de l\'agriculture durable : 14%.'
    )
    
    category = Category.objects.create(
        category = 'Fr:crudité'
    )

    product_with_category = ProductWithCategory.objects.create(
        product = product,
        category = category
    )
    
    expected_value = "Bouillon légumes knorr | Fr:crudité"
    
    assert str(product_with_category) == expected_value