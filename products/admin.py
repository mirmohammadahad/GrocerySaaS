from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'shop', 'created_at')
    search_fields = ('name', 'shop__name')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'shop', 'category', 'cost_price', 'selling_price', 'unit', 'is_active')
    list_filter = ('shop', 'category', 'is_active', 'unit')
    search_fields = ('name', 'barcode', 'sku', 'shop__name')