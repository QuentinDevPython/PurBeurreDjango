from django.db import models

from products.models import Product

class Favorites(models.Model):
    substitute = models.ForeignKey(Product, null=True, on_delete=models.CASCADE)
    date = models.DateTimeField(null=True)
