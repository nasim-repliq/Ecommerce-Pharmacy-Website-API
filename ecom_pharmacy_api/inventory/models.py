from django.db import models
from core.models import BaseModelUID

# Inventory model
class Inventory(BaseModelUID):
    product = models.ForeignKey('product.Product', on_delete=models.CASCADE)
    shop = models.ForeignKey('account.Organization', on_delete=models.CASCADE)
    stock_quantity = models.PositiveIntegerField()
    last_updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product.name} - {self.shop.shop_name}"
