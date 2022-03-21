from products.models import Product, Category, ProductWithCategory

from collections import Counter

class Substitute:
    
    def __init__(self, product_chosen):
        self.product_chosen = product_chosen
    
    def give_substitutes(self):
            
        id_product_chosen = self.product_chosen.id
        
        # Get the product_chosen categories id
        query_categories_chosen = ProductWithCategory.objects.filter(
            product=id_product_chosen
        )

        id_categories_chosen_dict = [
            item.category.id
            for item in query_categories_chosen
        ]
        
        # Get the products that are related at least with one of these categories
        query_products_substitute = []
        
        for id_category in id_categories_chosen_dict:
            query_products_substitute += [
                ProductWithCategory.objects.filter(
                    category=id_category
                )
            ]
        
        id_products_substitute = []
        
        for item in query_products_substitute:
            for item2 in item:
                if item2.product != self.product_chosen:
                    if self.product_chosen.grade <= 'B':
                        if item2.product.grade <= self.product_chosen.grade:
                            id_products_substitute += [
                                item2.product.id
                            ]
                    else:
                        if item2.product.grade < self.product_chosen.grade:
                            id_products_substitute += [
                                item2.product.id
                            ]
        
        # Count the categories in common for each product and returns the 6 firsts 
        substitute_most_common_categories = Counter(id_products_substitute).most_common(6)
        
        # Get the substitutes
        substitutes = []
        
        for item in substitute_most_common_categories:
            substitutes += [Product.objects.get(id=item[0])]

        #print(id_products_substitute)
        return substitutes
