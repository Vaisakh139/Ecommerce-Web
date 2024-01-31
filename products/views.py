from django.shortcuts import render
from .forms import Addproduct
from .models import Product
from django.core.paginator import Paginator

# Create your views here.

def index(request):
    featuerd_products = Product.objects.order_by('-priority')[:4]
    latest_products = Product.objects.order_by('-id')[:4]
    context = {
        'fea_produ' : featuerd_products,
        'late_produ' : latest_products
    }
    return render(request, 'index.html', context)


def list_products(request):

    page = 1
    if request.GET:
        page = request.GET.get('page',1)
    product_list = Product.objects.order_by('-priority')
    product_paginator = Paginator(product_list, 2)
    product_list = product_paginator.get_page(page)

    context ={'products' : product_list}
    return render(request, 'products.html', context)

def products_add(request):
    if request.POST:
        form = Addproduct(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'index.html')
    
    form = Addproduct()
    dict_ = {
        'form' : form
    }
    return render(request, 'products_add.html', dict_)


def detail_products(request):
    return render(request, 'products_details.html')


def product_desc(request, pk):
    product = Product.objects.get(pk=pk)
    context = {
        'product': product
    }
    return render(request, 'product_desc.html', context)