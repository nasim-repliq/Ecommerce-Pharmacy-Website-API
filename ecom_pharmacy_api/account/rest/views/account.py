from rest_framework import generics
from account.rest.serializers.account import OrganizationSerializer, PersonOrganizationSerializer
from account.models import Organization, PersonOrganization
from account.rest.permissions.account_permissions import *

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



# ----------------------------------------- Person Organization 

# List and create view for PersonOrganization
class PersonOrganizationListCreateView(generics.ListCreateAPIView):
    queryset = PersonOrganization.objects.all()
    serializer_class = PersonOrganizationSerializer
    permission_classes = [IsAdminOrStaffForWrite]  # Only admins or staff can create
    
    def perform_create(self, serializer):
        serializer.save()



# Retrieve, update, and delete view for PersonOrganization
class PersonOrganizationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PersonOrganization.objects.all()
    serializer_class = PersonOrganizationSerializer
    permission_classes = [IsAdminOrStaffForWrite]  # Only admins or staff can update or delete