from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Shop

@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'phone', 'is_active', 'created_at')
    search_fields = ('name', 'owner__username', 'phone')
    prepopulated_fields = {'slug': ('name',)}