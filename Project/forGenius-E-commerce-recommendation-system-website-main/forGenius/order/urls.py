from django.urls import path
from order.views import *

app_name = 'order'

urlpatterns = [
    path('cart/add/', add_to_cart, name='add_to_cart'),
    path('cart/view/', view_cart, name='view_cart'),
    path('cart/product_quantity/edit/', edit_cart_product_quantity, name='edit_cart_product_quantity'),
    path('cart/remove/', remove_cart_product, name='remove_cart_product'),
    path('create/', create_order, name='create_order'),
    path('view/', view_order, name='view_order'),
    path('pay/', pay_order, name='pay_order'),
    path('view/all/', view_all_order, name='view_all_order'),
    path('share/', share_order, name='share_order'),
    path('admin_view/all/', admin_view_all_order, name='admin_view_all_order'),
]
