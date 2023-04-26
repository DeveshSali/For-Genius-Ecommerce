from django.urls import path
from product.views import *

app_name = 'product'

urlpatterns = [
    path('user/view/', view_product_user, name='view_product_user'),
    path('add/', admin_add_product, name='admin_add_product'),
    path('edit/', admin_edit_product, name='admin_edit_product'),
    path('delete/', admin_delete_product, name='admin_delete_product'),
    path('all/', admin_products_all, name='admin_products_all'),
    path('all/sort/', admin_products_all_sort, name='admin_products_all_sort'),
    path('search/result/', get_search_result, name="get_search_result"),
    path('recommendation/public/', public_recommendation, name='public_recommendation'),
    path('recommendation/private/', private_recommendation, name='private_recommendation'),
]