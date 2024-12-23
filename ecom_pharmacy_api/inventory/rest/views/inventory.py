from rest_framework import mixins, generics
from rest_framework.permissions import SAFE_METHODS
from inventory.models import Inventory
from inventory.rest.serializers.inventory import InventorySerializer
from inventory.rest.permissions.inventory_permissions import IsAdminUser, IsOwner, IsAuthenticatedReadOnly


class InventoryListCreateView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer

    def get_permissions(self):
        if self.request.method in SAFE_METHODS:
            return [IsAuthenticatedReadOnly()]
        return [IsAdminUser() , IsOwner()]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class InventoryDetailView(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer

    def get_permissions(self):
        return [IsAdminUser() , IsOwner()]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
