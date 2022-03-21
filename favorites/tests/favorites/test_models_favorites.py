import pytest

from django.test import Client
from django.utils import timezone

from favorites.models import Favorites
from products.models import Product


class TestModelsFavorites:
    
    def setup_method(self, method):
        self.product = Product.objects.create(
            product_name_fr = 'Purée amande complète',
            countries = 'France,Switzerland',
            stores = 'biocoop',
            grade = 'A',
            url = 'https://fr.openfoodfacts.org/produit/3390390000122/puree-amande-complete-jean-herve',
            image_url = 'https://images.openfoodfacts.org/images/products/339/039/000/0122/front_fr.47.400.jpg',
            conservation_conditions_fr = '',
            additives_original_tags = '',
            allergens_from_ingredients = 'en:nuts, Amandes',
            ingredients_text_fr = '_Amandes_ complètes bio.'
        )
    

    @pytest.mark.django_db  
    def test_favorites_model(self):

        client = Client()

        now = timezone.now()
        
        favorite = Favorites.objects.create(
            substitute = self.product,
            date = now
        )

        expected_value = f"Purée amande complète | {now}"
        
        assert str(favorite) == expected_value
