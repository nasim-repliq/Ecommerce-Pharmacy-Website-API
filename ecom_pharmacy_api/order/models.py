from django.db import models
from autoslug import AutoSlugField
from core.models import BaseModelUID

# Order model
class Order(BaseModelUID):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('canceled', 'Canceled'),
    )
    PAYMENT_STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('paid', 'Paid'),
        ('failed', 'Failed'),
    )
    user = models.ForeignKey('core.Person', on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    payment_status = models.CharField(max_length=10, choices=PAYMENT_STATUS_CHOICES)
    shipping_address = models.TextField()
    order_date = models.DateTimeField()
    slug = AutoSlugField(populate_from='id', unique=True, always_update=False, null=True, blank=True)

    def __str__(self):
        return f"Order #{self.id} by {self.user.username}"


# OrderItem model
class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name="items", on_delete=models.CASCADE)
    product = models.ForeignKey('product.Product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)

    def save(self, *args, **kwargs):
        self.subtotal = self.unit_price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.product.name} (x{self.quantity})"


# DeliveryStatus model
class DeliveryStatus(BaseModelUID):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('in-transit', 'In-Transit'),
        ('delivered', 'Delivered'),
        ('canceled', 'Canceled'),
    )
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES)
    delivery_person = models.ForeignKey('core.Person', on_delete=models.CASCADE)
    delivery_date = models.DateTimeField()

    def __str__(self):
        return f"Delivery Status for Order #{self.order.id} ({self.status})"


# Cart model
class Cart(BaseModelUID):
    user = models.ForeignKey('core.Person', on_delete=models.CASCADE)
    slug = AutoSlugField(populate_from='id', unique=True, always_update=False, null=True, blank=True)

    def __str__(self):
        return f"Cart of {self.user.username}"


# CartItem model
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name="items", on_delete=models.CASCADE)
    product = models.ForeignKey('product.Product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    added_at = models.DateTimeField()
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.subtotal = self.unit_price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.product.name} (x{self.quantity})"

