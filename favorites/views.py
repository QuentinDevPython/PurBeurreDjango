from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.utils import timezone

from favorites.my_food import MyFood

from products.search_product import SearchProduct

from products import forms


@login_required
def my_food(request, product):
    
    search_form = forms.SearchForm()
    if request.method == 'POST':
        search_form = forms.SearchForm(request.POST)
        if search_form.is_valid():
            product_searched = request.POST['product'].lower()
            return redirect('products', product_searched)
        
    if product.startswith('@'):
        product = product[1:]
        try:
            product = SearchProduct(product).search_product()
            MyFood().delete_favorite(product)
            product = 'None'
        except:
            pass
    
    if product == 'None':
        result = MyFood().get_favorites().order_by('-date')

        result_list = []
        for item in result:
            result_list += [SearchProduct(item.substitute).search_product()]

        result = result_list
        
        paginator = Paginator(result, 6)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
    
        return render(
            request,
            'favorites/my_food.html',
            context={
                'result':result,
                'page_obj':page_obj,
                'search_form':search_form,
            }
        )

    product = SearchProduct(product).search_product() 
    now = timezone.now()
    MyFood().create_new_favorite(product, now)
    
    result = MyFood().get_favorites().order_by('-date')

    result_list = []
    for item in result:
        result_list += [SearchProduct(item.substitute).search_product()]

    result = result_list
    
    paginator = Paginator(result, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(
        request,
        'favorites/my_food.html',
        context={
            'result':result,
            'page_obj':page_obj,
            'search_form':search_form,
        }
    )
