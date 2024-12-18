from django.shortcuts import render

from rest_framework import generics
from .models import *
from .serializers import PersonSerializer, OrganizationSerializer, ProductSerializer, PersonOrganizationSerializer, CategorySerializer, InventorySerializer, OrderSerializer, OrderItemSerializer, DeliveryStatusSerializer, CartStatusSerializer, CartItemSerializer, ReviewSerializer

from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.filters import SearchFilter

from .permissions import *


#---------------------------------- Person 
# Create a Person view for listing and creating users
class PersonListCreateView(generics.ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    permission_classes = [IsAdminOrReadOnly]  # Custom permission for the view

    def perform_create(self, serializer):
        serializer.save() 


# Retrieve, update, and delete Person
class PersonDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can access this view


#----------------------------------  Organization
# Organization Views
class OrganizationListCreateView(generics.ListCreateAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    permission_classes = [IsAdminOrStaffForWrite]



class OrganizationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    permission_classes = [IsAdminOrStaffForWrite]



#----------------------------------  Product
# Product Views
class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name', 'description']


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
