import pytest

from django.urls import reverse, resolve

from products.models import Product


class TestUrlsFavorites:

    def setup_method(self, method):
        self.product = Product.objects.create(
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

 
    @pytest.mark.django_db
    def test_my_food_url(self):
        
        path = reverse(
            'my_food',
            kwargs={
                'product': self.product
            }
        )
        
        assert path == "/favorites/my_food/Formule%20boost/"
        assert resolve(path).view_name == "my_food"
