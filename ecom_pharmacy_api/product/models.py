from django.db import models
from autoslug import AutoSlugField
from versatileimagefield.fields import VersatileImageField
from core.models import BaseModelUID

# Category model
class Category(BaseModelUID):
    name = models.CharField(max_length=255)
    description = models.TextField()
    slug = AutoSlugField(populate_from='name', unique=True, always_update=False, null=True, blank=True)

    def __str__(self):
        return self.name


# Product model
class Product(BaseModelUID):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    expiry_date = models.DateField()
    shop = models.ForeignKey('account.Organization', on_delete=models.CASCADE)
    image = VersatileImageField(upload_to='products/', blank=True, null=True)
    slug = AutoSlugField(populate_from='name', unique=True, always_update=False, null=True, blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        indexes = [
            models.Index(fields=['category', 'shop']),
        ]


# Review model
class Review(BaseModelUID):
    user = models.ForeignKey('core.Person', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField()
    review_text = models.TextField()
    slug = AutoSlugField(populate_from='id', unique=True, always_update=False, null=True, blank=True)

    def __str__(self):
        return f"Review by {self.user.username} for {self.product.name}"
