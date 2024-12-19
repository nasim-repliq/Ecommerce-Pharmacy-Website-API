from django.contrib import admin
from .models import *

# Register Organization model
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('shop_name', 'address', 'phone_number', 'created_at', 'updated_at')
    search_fields = ('shop_name', 'phone_number')
    list_filter = ('created_at', 'updated_at')
    ordering = ('shop_name',)

admin.site.register(Organization, OrganizationAdmin)

# Register PersonOrganization model
class PersonOrganizationAdmin(admin.ModelAdmin):
    list_display = ('user', 'shop', 'role', 'created_at', 'updated_at')
    search_fields = ('user__username', 'shop__shop_name', 'role')
    list_filter = ('role', 'created_at')
    ordering = ('shop', 'role')

admin.site.register(PersonOrganization, PersonOrganizationAdmin)
