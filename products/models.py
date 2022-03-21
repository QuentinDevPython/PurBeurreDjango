from django.db import models
from django.db.models import CharField
from django.db.models.functions import Lower

CharField.register_lookup(Lower)
class Product(models.Model):
    
    class Meta:
        ordering = ['grade']

    def __str__(self):
        return f'{self.product_name_fr}'
    
    class Grade(models.TextChoices):
        A = 'A'
        B = 'B'
        C = 'C'
        D = 'D'
        E = 'E'

    product_name_fr = models.fields.CharField(max_length=100)
    countries = models.fields.CharField(max_length=400)
    stores = models.fields.CharField(max_length=150)
    grade = models.fields.CharField(choices=Grade.choices, max_length=1)
    url = models.fields.CharField(max_length=300)
    image_url = models.fields.CharField(max_length=300)
    conservation_conditions_fr = models.fields.CharField(max_length=500, null=True)
    additives_original_tags = models.fields.CharField(max_length=400, null=True)
    allergens_from_ingredients = models.fields.CharField(max_length=400, null=True)
    ingredients_text_fr = models.fields.CharField(max_length=2000, null=True)

class Category(models.Model):
    
    def __str__(self):
        return f'{self.category}'
    
    category = models.fields.CharField(max_length=500)
    
class ProductWithCategory(models.Model):
    product = models.ForeignKey(Product, null=True, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, null=True, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.product} | {self.category}'
