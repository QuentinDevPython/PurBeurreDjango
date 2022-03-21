from favorites.models import Favorites

class MyFood:
    
    def __init__(self):
        pass
    
    def create_new_favorite(self, product, now):

        try :
            product = Favorites.objects.get(
                substitute=product
            )
            product.date = now
            product.save()
        except:
            Favorites.objects.create(
                substitute=product,
                date=now
            )
        
    def get_favorites(self):
        return Favorites.objects.all()
    
    def delete_favorite(self, product):
        product = Favorites.objects.filter(
            substitute = product.id
        ).delete()