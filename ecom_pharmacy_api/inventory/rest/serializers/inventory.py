from rest_framework import serializers
from inventory.models import Inventory


class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = ['id', 'product', 'shop', 'stock_quantity', 'last_updated']