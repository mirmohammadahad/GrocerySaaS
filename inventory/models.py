from django.db import models
from products.models import Product


class StockAdjustment(models.Model):

    ADJUSTMENT_TYPES = [
        ('IN', 'Stock In'),
        ('OUT', 'Stock Out'),
        ('DAMAGE', 'Damaged'),
        ('CORRECTION', 'Correction'),
    ]

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='stock_adjustments'
    )

    adjustment_type = models.CharField(
        max_length=20,
        choices=ADJUSTMENT_TYPES
    )

    quantity = models.PositiveIntegerField()

    reason = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product.name} - {self.adjustment_type} - {self.quantity}"