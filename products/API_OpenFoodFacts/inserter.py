"""Import the module tqdm to add a loading bar"""
from tqdm import tqdm

class Inserter:
    """
    Class that inserts the data collected and cleaned into the database by 
    calling the functions defined in Inserter_functions class

    Args:
        cleaned_data (str dictionnary)
        Products (table of the database)
        Categories (table of the database)
        Products_with_Categories (table of the database)
    """
    def __init__(self, cleaned_data, Product, Category, ProductWithCategory):
        self.cleaned_data = cleaned_data
        self.Category = Category
        self.Product = Product
        self.ProductWithCategory = ProductWithCategory
    
    def insert_data(self):
        """
        Method that inserts the data collected and cleaned into the database
        """
        for data in tqdm(self.cleaned_data):
            
            try:
                product = self.Product.objects.get(
                    product_name_fr = data["product_name_fr"],
                )

            except self.Product.DoesNotExist:
                if not data.get("conservation_conditions_fr"):
                    data["conservation_conditions_fr"] = ""
                if not data.get("ingredients_text_fr"):
                    data["ingredients_text_fr"] = ""
                if not data.get("additives_original_tags"):
                    data["additives_original_tags"] = ""
                if not data.get("allergens_from_ingredients"):
                    data["allergens_from_ingredients"] = ""
                
                product = self.Product.objects.create(
                    product_name_fr = data["product_name_fr"],
                    countries = data["countries"],
                    stores = data["stores"],
                    grade = data["nutriscore_grade"],
                    url = data["url"],
                    image_url = data["image_url"],
                    conservation_conditions_fr = data["conservation_conditions_fr"],
                    additives_original_tags = data["additives_original_tags"],
                    allergens_from_ingredients = data["allergens_from_ingredients"],
                    ingredients_text_fr = data["ingredients_text_fr"]
                )

            categories = data["categories"].split(",")
            
            for item in categories:
                category = self.Category.objects.get_or_create(
                    category = item
                )
            
            for item in categories:
                
                try:
                    categorized = self.ProductWithCategory.objects.get_or_create(
                        product = self.Product.objects.get(
                            product_name_fr = data["product_name_fr"],
                        ),
                        category = self.Category.objects.get(
                            category = item
                        )
                    )
                except self.Product.MultipleObjectsReturned:
                    print("Model.MultipleObjectsReturned")
                except self.Product.DoesNotExist:
                    print("DoesNotExist")