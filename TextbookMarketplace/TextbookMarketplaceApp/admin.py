from django.contrib import admin
from django.contrib.auth.models import User # Importáld a User modellt vagy az általad használt modellt
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'file', 'institution', 'subject', 'description')  # Válaszd ki, mely mezőket szeretnéd megjeleníteni a listázáskor

