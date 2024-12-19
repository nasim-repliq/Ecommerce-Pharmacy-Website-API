from rest_framework import serializers
from .models import Person
from django.core.validators import EmailValidator
import re


class PersonSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = Person
        fields = [
            'id', 'username', 'slug', 'first_name', 'last_name', 'email', 'phone_number', 'password',
            'address', 'profile_picture'
        ]
    
    def validate_email(self, value):
        if Person.objects.filter(email=value).exists():
            raise serializers.ValidationError("This email is already registered.")
        EmailValidator()(value)
        return value

    def validate_phone_number(self, value):
        phone_pattern = r'^\+?\d{10,15}$'
        if not re.match(phone_pattern, value):
            raise serializers.ValidationError("Enter a valid phone number.")
        return value

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = Person.objects.create_user(**validated_data) 
        user.set_password(password)
        user.save()
        return user





# class PersonSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Person
#         fields = ['id', 'username', 'slug', 'first_name', 'last_name', 'email', 'phone_number', 'address']
    
#     # Custom validation for email
#     def validate_email(self, value):
#         # Check if email is unique
#         if Person.objects.filter(email=value).exists():
#             raise serializers.ValidationError("This email is already registered.")
#         # You can add additional email validation logic here if needed
#         EmailValidator()(value)  # Using Django's EmailValidator for email format
#         return value

#     # Custom validation for password
#     def validate_password(self, value):
#         # Check password strength (minimum 8 characters, one uppercase, one lowercase, one digit)
#         if len(value) < 8:
#             raise serializers.ValidationError("Password must be at least 8 characters long.")
#         if not re.search(r"[A-Z]", value):
#             raise serializers.ValidationError("Password must contain at least one uppercase letter.")
#         if not re.search(r"[a-z]", value):
#             raise serializers.ValidationError("Password must contain at least one lowercase letter.")
#         if not re.search(r"\d", value):
#             raise serializers.ValidationError("Password must contain at least one digit.")
#         return value

#     # Custom validation for username (unique check)
#     def validate_username(self, value):
#         if Person.objects.filter(username=value).exists():
#             raise serializers.ValidationError("This username is already taken.")
#         return value

#     # Custom validation for phone_number (optional, you can adjust the validation pattern)
#     def validate_phone_number(self, value):
#         phone_pattern = r'^\+?\d{10,15}$'  # Example: Match international phone numbers (10-15 digits)
#         if not re.match(phone_pattern, value):
#             raise serializers.ValidationError("Enter a valid phone number.")
#         return value
    
#     # Optional: You can also override the `create` method if you want to modify data before saving
#     def create(self, validated_data):
#         validated_data['password'] = self.context['request'].data['password']  # Ensure password is handled securely
#         person = Person.objects.create(**validated_data)
#         person.set_password(validated_data['password'])  # Hash the password before saving
#         person.save()
#         return person



# # --------------------Organization Serializer
# class OrganizationSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Organization
#         fields = ['shop_name', 'address', 'phone_number', 'logo', 'slug', 'created_at', 'updated_at']

# # ----------------------Product Serializer
# class ProductSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Product
#         fields = '__all__'

#         def validate_price(self, value):
#             if value <= 0:
#                 raise serializers.ValidationError("Price must be greater than 0.")
#             return value

# # ----------------------- PersonOrganization
# class PersonOrganizationSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = PersonOrganization
#         fields = ['id', 'user', 'shop', 'role']

# #---------------------------------- Category
# class CategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Category
#         fields = '__all__'


# #---------------------------------- Inventory
# class InventorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Inventory
#         fields = '__all__'

# #----------------------------------  Order 
# class OrderSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Order
#         fields = '__all__'

# #----------------------------------  OrderItem
# class OrderItemSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = OrderItem
#         fields = '__all__'


# #----------------------------------  Delivery
# class DeliveryStatusSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = DeliveryStatus
#         fields = '__all__'


# #----------------------------------  Cart
# class CartStatusSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Cart
#         fields = '__all__'

# #----------------------------------  CartItem
# class CartItemSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CartItem
#         fields = '__all__'

# #----------------------------------  Review 
# class ReviewSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Review
#         fields = '__all__'
