from django.urls import path
from . import views

urlpatterns = [
    path('order', views.show_cart, name='cart'),
    path('add_cart', views.add_to_cart, name='add_to_cart')

]
