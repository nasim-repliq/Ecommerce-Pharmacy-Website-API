from django.db import models

from django.db import models
from autoslug import AutoSlugField
from versatileimagefield.fields import VersatileImageField
from core.models import BaseModelUID

# Organization model
class Organization(BaseModelUID):
    shop_name = models.CharField(max_length=255)
    address = models.TextField()
    phone_number = models.CharField(max_length=15)
    logo = VersatileImageField(upload_to='organization_logos/', blank=True, null=True)
    slug = AutoSlugField(populate_from='shop_name', unique=True, always_update=False, null=True, blank=True)

    def __str__(self):
        return self.shop_name


# PersonOrganization model
class PersonOrganization(BaseModelUID):
    ROLE_CHOICES = (
        ('owner', 'Owner'),
        ('employee', 'Employee'),
        ('manager', 'Manager'),
    )
    user = models.ForeignKey('core.Person', on_delete=models.CASCADE)
    shop = models.ForeignKey(Organization, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.user.username} - {self.shop.shop_name} ({self.role})"
