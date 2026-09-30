import uuid
from django.db import models

class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    shop = models.ForeignKey('shops.Shop', on_delete=models.CASCADE, related_name='categories')
    name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Categories"
        unique_together = ('shop', 'slug')

    def __str__(self):
        return f"{self.name} - ({self.shop.name})"


class Product(models.Model):
    UNIT_CHOICES = [
        ('KG', 'Kilogram'),
        ('PCS', 'Pieces'),
        ('LIT', 'Liter'),
        ('BOX', 'Box'),
        ('PKT', 'Packet'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    shop = models.ForeignKey('shops.Shop', on_delete=models.CASCADE, related_name='products')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='products')
    
    name = models.CharField(max_length=255)
    sku = models.CharField(max_length=100, blank=True, null=True)
    barcode = models.CharField(max_length=100, blank=True, null=True)
    
    cost_price = models.DecimalField(max_digits=10, decimal_places=2, help_text="ক্রয়মূল্য")
    selling_price = models.DecimalField(max_digits=10, decimal_places=2, help_text="বিক্রয়মূল্য")
    
    unit = models.CharField(max_length=10, choices=UNIT_CHOICES, default='PCS')
    is_active = models.BooleanField(default=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('shop', 'barcode')

    def __str__(self):
        return f"{self.name} - {self.selling_price} BDT"