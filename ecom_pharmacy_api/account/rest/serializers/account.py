from rest_framework import serializers
from account.models import Organization, PersonOrganization

class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = '__all__'


class PersonOrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonOrganization
        fields = '__all__'
