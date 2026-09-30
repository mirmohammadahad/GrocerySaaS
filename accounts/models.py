from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    class Role(models.TextChoices):
        SUPER_ADMIN = 'SUPER_ADMIN', 'Super Admin'
        SHOP_OWNER = 'SHOP_OWNER', 'Shop Owner'
        SHOP_MANAGER = 'SHOP_MANAGER', 'Shop Manager'
        CASHIER = 'CASHIER', 'Cashier'

    role = models.CharField(
        max_length=20, 
        choices=Role.choices, 
        default=Role.SHOP_OWNER
    )
    shop = models.ForeignKey(
        'shops.Shop', 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        related_name='employees'
    )
    phone_number = models.CharField(max_length=15, unique=True, null=True, blank=True)
    is_active_user = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"