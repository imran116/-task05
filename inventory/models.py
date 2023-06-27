from django.db import models

from inventory.constant import StockStatus


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    desc = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    qty = models.IntegerField(default=0)
    price = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
    stock_status = models.SmallIntegerField(choices=StockStatus.choices, default=StockStatus.IN_STOCK)

    def __str__(self):
        return self.name
