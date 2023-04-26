from django.contrib import admin
from django.contrib.admin.options import csrf_protect_m
from .models import Product, Features

# Register your models here.
admin.site.register(Product)
admin.site.register(Features)