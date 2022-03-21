import pytest

from django.urls import reverse, resolve

from products.models import Product


class TestUrlsProducts:
    
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
        self.product_searched = 'cacao nesquik'
        

    @pytest.mark.django_db
    def test_home_url(self):

        path = reverse('home')
        assert path == "/home/"
        assert resolve(path).view_name == "home"

        
    @pytest.mark.django_db
    def test_products_url(self):
        
        path = reverse(
            'products',
            kwargs={
                'product_searched': self.product_searched
            }
        )
        
        assert path == "/products/cacao%20nesquik/"
        assert resolve(path).view_name == "products"


    @pytest.mark.django_db
    def test_product_details_url(self):
        
        path = reverse(
            'product_details',
            kwargs={
                'product': self.product
            }
        )
        
        assert path == "/products/detail/Formule%20boost/"
        assert resolve(path).view_name == "product_details"

 
    @pytest.mark.django_db
    def test_substitute_url(self):
        
        path = reverse(
            'substitute',
            kwargs={
                'product': self.product
            }
        )
        
        assert path == "/products/substitute/Formule%20boost/"
        assert resolve(path).view_name == "substitute"
        