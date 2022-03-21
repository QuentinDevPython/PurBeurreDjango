from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

from products.search_product import SearchProduct
from products.substitute import Substitute

from . import forms

def home(request):
    search_form = forms.SearchForm()
    product_form = forms.ProductForm()
    if request.method == 'POST':
        search_form = forms.SearchForm(request.POST)
        product_form = forms.ProductForm(request.POST)
        if product_form.is_valid():
            product_searched = request.POST['product'].lower()
            return redirect('products', product_searched)

    return render(
        request,
        'products/home.html',
        context={
            'product_form': product_form,
            'search_form': search_form
        }
    )

@login_required
def products(request, product_searched):
    result = SearchProduct(product_searched).search_corresponding_products()
    search_form = forms.SearchForm()
    if request.method == 'POST':
        search_form = forms.SearchForm(request.POST)
        if search_form.is_valid():
            product_searched = request.POST['product'].lower()
            return redirect('products', product_searched)
    
    paginator = Paginator(result, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        'products/products.html',
        context={
            'result':result,
            'page_obj':page_obj,
            'product_searched':product_searched,
            'search_form': search_form,
        }
    )
    
@login_required
def product_details(request, product):
    product = SearchProduct(product).search_product()
    search_form = forms.SearchForm()
    if request.method == 'POST':
        search_form = forms.SearchForm(request.POST)
        if search_form.is_valid():
            product_searched = request.POST['product'].lower()
            return redirect('products', product_searched)
        
    return render(
        request,
        'products/product_details.html',
        context={
            'search_form':search_form,
            'product': product,
        }
    )

@login_required
def substitute(request, product):
    product = SearchProduct(product).search_product()
    result = Substitute(product).give_substitutes()
    search_form = forms.SearchForm()
    if request.method == 'POST':
        search_form = forms.SearchForm(request.POST)
        if search_form.is_valid():
            product_searched = request.POST['product'].lower()
            return redirect('products', product_searched)
        
    return render(
        request,
        'products/substitute.html',
        context={
            'product':product,
            'search_form':search_form,
            'result': result,
        }
    )

