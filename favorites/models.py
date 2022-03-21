from django.db import models

from products.models import Product

class Favorites(models.Model):
    
    def __str__(self):
        return f'{self.substitute} | {self.date}'
    
    substitute = models.ForeignKey(Product, null=True, on_delete=models.CASCADE)
    date = models.DateTimeField(null=True)
