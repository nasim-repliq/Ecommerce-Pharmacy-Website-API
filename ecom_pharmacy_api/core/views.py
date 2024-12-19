from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import PersonSerializer
from .permissions import *

# OrganizationSerializer, ProductSerializer, PersonOrganizationSerializer, CategorySerializer, InventorySerializer, OrderSerializer, OrderItemSerializer, DeliveryStatusSerializer, CartStatusSerializer, CartItemSerializer, ReviewSerializer

# from rest_framework.permissions import IsAuthenticated
# from rest_framework.filters import SearchFilter



# Create a Person view for listing and creating users
class PersonListCreateView(generics.ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    permission_classes = [IsOwnerOrAdmin]  # custom permission

    def get_queryset(self):
        # Restrict list access to admin/staff only
        if self.request.user and (self.request.user.is_staff or self.request.user.is_superuser):
            return super().get_queryset()
        return Person.objects.none()  # Non-admin users can't see the list


class PersonDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    permission_classes = [IsOwnerOrAdmin]  # Apply the custom permission




# #----------------------------------  Organization
# # Organization Views
# class OrganizationListCreateView(generics.ListCreateAPIView):
#     queryset = Organization.objects.all()
#     serializer_class = OrganizationSerializer
#     permission_classes = [IsAdminOrStaffForWrite]



# class OrganizationDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Organization.objects.all()
#     serializer_class = OrganizationSerializer
#     permission_classes = [IsAdminOrStaffForWrite]



# # ----------------------------------------- Person Organization 

# # List and create view for PersonOrganization
# class PersonOrganizationListCreateView(generics.ListCreateAPIView):
#     queryset = PersonOrganization.objects.all()
#     serializer_class = PersonOrganizationSerializer
#     permission_classes = [IsAdminOrStaffForWrite]  # Only admins or staff can create
    
#     def perform_create(self, serializer):
#         serializer.save()



# # Retrieve, update, and delete view for PersonOrganization
# class PersonOrganizationDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = PersonOrganization.objects.all()
#     serializer_class = PersonOrganizationSerializer
#     permission_classes = [IsAdminOrStaffForWrite]  # Only admins or staff can update or delete

# #----------------------------------  Product
# # Product Views
# class ProductListCreateView(generics.ListCreateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     filter_backends = [SearchFilter]
#     search_fields = ['name', 'description']


# class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
