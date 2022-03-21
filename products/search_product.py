import random
import unidecode

from products.models import Product

class SearchProduct:
    
    def __init__(self, product_searched):
        self.product_searched = product_searched
    
    def get_max_common(self, products_found_table):
        max_common = 0
        for number in range(len(products_found_table)):
            if products_found_table[number][1] > max_common:
                max_common = products_found_table[number][1]
        return max_common
    
    def select_products_found(self, products_found_returned, products_found_table, max_common):
        for number in range(len(products_found_table)):
            if products_found_table[number][1] == max_common:
                products_found_returned += [products_found_table[number][0]]
            
        for product in products_found_returned:
            for number in range(len(products_found_table)):
                if products_found_table[number][0] == product:
                    products_found_table.remove(
                        [
                            products_found_table[number][0],
                            products_found_table[number][1]
                        ]
                    )
                    break
    
    def search_corresponding_products(self):
        product_searched_list = self.product_searched.split(' ')

        products_found_table = [] 
        for element in product_searched_list:
            products_found = Product.objects.filter(product_name_fr__lower__unaccent__contains=unidecode.unidecode(element))
            for item in products_found:
                product_in_table = False
                for number in range(len(products_found_table)):
                    if item == products_found_table[number][0]:
                        products_found_table[number][1] += 1
                        product_in_table = True
                if product_in_table is not True:
                    products_found_table += [[item, 1]]
        
        max_common = self.get_max_common(products_found_table)
        
        products_found_returned = []
        self.select_products_found(products_found_returned, products_found_table, max_common)
                
        while len(products_found_returned) < 6:
            
            max_common = self.get_max_common(products_found_table)
            
            if max_common == 0 or len(products_found_table)==0:
                break

            if max_common == 1:
                number = random.randint(0, len(products_found_table)-1)
                products_found_returned += [products_found_table[number][0]]
                products_found_table.remove(
                    [
                        products_found_table[number][0],
                        products_found_table[number][1]
                    ]
                )
            else:
                
                self.select_products_found(products_found_returned, products_found_table, max_common)

        return products_found_returned
    
    def search_product(self):
        return Product.objects.get(product_name_fr=self.product_searched)