from django.urls import path
from . import views

urlpatterns = [
        path('',views.index, name='home'),
        path('product_list',views.list_products, name='list_products'),
        path('product_desc/<pk>',views.product_desc, name='products_desc'),
        path('addP',views.products_add, name='productsAdd'),
]