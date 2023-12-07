from django.contrib import admin

from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('institution', 'name', 'subject', 'description', 'price', 'category', 'is_available', 'image')
