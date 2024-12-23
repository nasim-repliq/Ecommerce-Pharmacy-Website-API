from django.urls import path
from inventory.rest.views.inventory import InventoryListCreateView, InventoryDetailView

urlpatterns = [
    path('', InventoryListCreateView.as_view(), name='inventory-list-create'),
    path('<uuid:pk>', InventoryDetailView.as_view(), name='inventory-detail'),
]
