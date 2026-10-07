from django.db import models
from shops.models import Shop


class Category(models.Model):
    shop = models.ForeignKey(
        Shop,
        on_delete=models.CASCADE,
        related_name='categories'
    )
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Categories"
        unique_together = ('shop', 'slug')

    def __str__(self):
        return self.name


class Product(models.Model):
    shop = models.ForeignKey(
        Shop,
        on_delete=models.CASCADE,
        related_name='products'
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='products'
    )

    name = models.CharField(max_length=200)

    barcode = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    sku = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    unit = models.CharField(
        max_length=50,
        default='piece'
    )

    quantity = models.PositiveIntegerField(default=0)

    cost_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    selling_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    low_stock_threshold = models.PositiveIntegerField(default=5)

    is_active = models.BooleanField(default=True)

    @property
    def is_low_stock(self):
        return self.quantity <= self.low_stock_threshold

    def __str__(self):
        return self.name