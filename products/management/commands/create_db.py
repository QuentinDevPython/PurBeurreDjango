from django.core.management.base import BaseCommand

from products.API_OpenFoodFacts.downloader import Downloader
from products.API_OpenFoodFacts.cleaner import Cleaner
from products.API_OpenFoodFacts.inserter import Inserter

from products.models import Product, Category, ProductWithCategory

class Command(BaseCommand):
    help = 'Fill the database with OpenFoodFacts products'

    def handle(self, *args, **kwargs):
        
        try:
            downloader = Downloader()
            all_data = downloader.get_all_data()
            
            cleaner = Cleaner(all_data)
            cleaned_data = cleaner.get_cleaned_data()
            
            inserter = Inserter(
                   cleaned_data,
                   Product,
                   Category,
                   ProductWithCategory
               )
            inserter.insert_data()

            self.stdout.write(
                self.style.SUCCESS(
                    "The products have been successfully imported !"
                )
            )
        except:
            self.stdout.write(
                self.style.ERROR(
                    "Error. There was a problem importing the products. Please try again."
                )
            )
