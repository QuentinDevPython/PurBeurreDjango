import pytest

from django.test import Client
from products.models import Product, Category, ProductWithCategory


class TestModelsProducts:
    
    def setup_method(self, method):
        self.product = Product.objects.create(
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
        
        self.category = Category.objects.create(
            category = 'Chocolat-au-lait-aux-morceaux-de-biscuits'
        )

     
    @pytest.mark.django_db  
    def test_product_model(self):
        client = Client()

        expected_value = "Ricore original, café & chicorée, boîte 100g"
        
        assert str(self.product) == expected_value


    @pytest.mark.django_db  
    def test_category_model(self):

        client = Client()
        
        expected_value = "Chocolat-au-lait-aux-morceaux-de-biscuits"
        
        assert str(self.category) == expected_value


    @pytest.mark.django_db  
    def test_product_with_category_model(self):

        client = Client()

        product_with_category = ProductWithCategory.objects.create(
            product = self.product,
            category = self.category
        )
        
        expected_value = "Ricore original, café & chicorée, boîte 100g | Chocolat-au-lait-aux-morceaux-de-biscuits"
        
        assert str(product_with_category) == expected_value
