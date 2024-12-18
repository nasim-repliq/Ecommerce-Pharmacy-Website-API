from django.db import models
from django.contrib.auth.models import AbstractUser


# Abstract BaseModel with common fields
class BaseModelUID(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

        
# Person model
class Person(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    # USERNAME_FIELD = 'email' 
    REQUIRED_FIELDS = ['email', 'phone_number', 'address', 'first_name']  
    
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"


# Organization model
class Organization(BaseModelUID):
    shop_name = models.CharField(max_length=255)
    address = models.TextField()
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.shop_name


# PersonOrganization 
class PersonOrganization(BaseModelUID):
    ROLE_CHOICES = (
        ('owner', 'Owner'),
        ('employee', 'Employee'),
        ('manager', 'Manager'),
    )
    user = models.ForeignKey(Person, on_delete=models.CASCADE)
    shop = models.ForeignKey(Organization, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    
    def __str__(self):
        return f"{self.user.username} - {self.shop.shop_name} ({self.role})"


# Category model
class Category(BaseModelUID):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name


# Product model
class Product(BaseModelUID):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    expiry_date = models.DateField()
    shop = models.ForeignKey(Organization, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    class Meta:
        indexes = [
            models.Index(fields=['category', 'shop']),
        ]


# Inventory model
class Inventory(BaseModelUID):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    shop = models.ForeignKey(Organization, on_delete=models.CASCADE)
    stock_quantity = models.PositiveIntegerField()
    last_updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product.name} - {self.shop.shop_name}"


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
    user = models.ForeignKey(Person, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    payment_status = models.CharField(max_length=10, choices=PAYMENT_STATUS_CHOICES)
    shipping_address = models.TextField()
    order_date = models.DateTimeField()

    def __str__(self):
        return f"Order #{self.id} by {self.user.username}"


# OrderItem model 
class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name="items", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
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
    delivery_person = models.ForeignKey(Person, on_delete=models.CASCADE)
    delivery_date = models.DateTimeField()

    def __str__(self):
        return f"Delivery Status for Order #{self.order.id} ({self.status})"


# Cart model
class Cart(BaseModelUID):
    user = models.ForeignKey(Person, on_delete=models.CASCADE)

    def __str__(self):
        return f"Cart of {self.user.username}"


# CartItem model 
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name="items", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    added_at = models.DateTimeField()
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True) 


    def save(self, *args, **kwargs):
        self.subtotal = self.unit_price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.product.name} (x{self.quantity})"


# Review model
class Review(BaseModelUID):
    user = models.ForeignKey(Person, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField()
    review_text = models.TextField()

    def __str__(self):
        return f"Review by {self.user.username} for {self.product.name}"
