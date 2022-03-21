from csv import list_dialects
from django.contrib import admin

from products.models import Product, Category, ProductWithCategory

class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name_fr', 'grade', 'stores')

admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(ProductWithCategory)