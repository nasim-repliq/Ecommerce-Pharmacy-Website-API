from django.contrib import admin

from .models import Person
# Organization, PersonOrganization, Category, Product, Inventory, Order, OrderItem, DeliveryStatus, Cart, CartItem, Review

# Register Person model
class PersonAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email', 'phone_number', 'address', 'is_active', 'is_staff')
    search_fields = ('username', 'email', 'first_name', 'last_name', 'phone_number')
    list_filter = ('is_active', 'is_staff')
    ordering = ('username',)

admin.site.register(Person, PersonAdmin)

# # Register Organization model
# class OrganizationAdmin(admin.ModelAdmin):
#     list_display = ('shop_name', 'address', 'phone_number', 'created_at', 'updated_at')
#     search_fields = ('shop_name', 'phone_number')
#     list_filter = ('created_at', 'updated_at')
#     ordering = ('shop_name',)

# admin.site.register(Organization, OrganizationAdmin)

# # Register PersonOrganization model
# class PersonOrganizationAdmin(admin.ModelAdmin):
#     list_display = ('user', 'shop', 'role', 'created_at', 'updated_at')
#     search_fields = ('user__username', 'shop__shop_name', 'role')
#     list_filter = ('role', 'created_at')
#     ordering = ('shop', 'role')

# admin.site.register(PersonOrganization, PersonOrganizationAdmin)

# # Register Category model
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ('name', 'description', 'created_at', 'updated_at')
#     search_fields = ('name', 'description')
#     ordering = ('name',)

# admin.site.register(Category, CategoryAdmin)

# # Register Product model
# class ProductAdmin(admin.ModelAdmin):
#     list_display = ('name', 'category', 'price', 'shop', 'expiry_date', 'created_at', 'updated_at')
#     search_fields = ('name', 'category__name', 'shop__shop_name')
#     list_filter = ('category', 'shop', 'expiry_date')
#     ordering = ('name',)

# admin.site.register(Product, ProductAdmin)

# # Register Inventory model
# class InventoryAdmin(admin.ModelAdmin):
#     list_display = ('product', 'shop', 'stock_quantity', 'last_updated')
#     search_fields = ('product__name', 'shop__shop_name')
#     list_filter = ('shop', 'last_updated')
#     ordering = ('product',)

# admin.site.register(Inventory, InventoryAdmin)

# # Register Order model
# class OrderAdmin(admin.ModelAdmin):
#     list_display = ('user', 'total_price', 'status', 'payment_status', 'order_date', 'shipping_address')
#     search_fields = ('user__username', 'status', 'payment_status')
#     list_filter = ('status', 'payment_status', 'order_date')
#     ordering = ('order_date',)

# admin.site.register(Order, OrderAdmin)

# # Register OrderItem model
# class OrderItemAdmin(admin.ModelAdmin):
#     list_display = ('order', 'product', 'quantity', 'unit_price', 'subtotal')
#     search_fields = ('order__id', 'product__name')
#     list_filter = ('order', 'product')
#     ordering = ('order',)

# admin.site.register(OrderItem, OrderItemAdmin)

# # Register DeliveryStatus model
# class DeliveryStatusAdmin(admin.ModelAdmin):
#     list_display = ('order', 'status', 'delivery_person', 'delivery_date')
#     search_fields = ('order__id', 'status', 'delivery_person__username')
#     list_filter = ('status', 'delivery_person', 'delivery_date')
#     ordering = ('delivery_date',)

# admin.site.register(DeliveryStatus, DeliveryStatusAdmin)

# # Register Cart model
# class CartAdmin(admin.ModelAdmin):
#     list_display = ('user', 'created_at', 'updated_at')
#     search_fields = ('user__username',)
#     ordering = ('user',)

# admin.site.register(Cart, CartAdmin)

# # Register CartItem model
# class CartItemAdmin(admin.ModelAdmin):
#     list_display = ('cart', 'product', 'quantity', 'unit_price', 'added_at', 'subtotal')
#     search_fields = ('cart__id', 'product__name')
#     list_filter = ('cart', 'product')
#     ordering = ('cart',)

# admin.site.register(CartItem, CartItemAdmin)

# # Register Review model
# class ReviewAdmin(admin.ModelAdmin):
#     list_display = ('user', 'product', 'rating', 'review_text', 'created_at')
#     search_fields = ('user__username', 'product__name')
#     list_filter = ('rating', 'created_at')
#     ordering = ('created_at',)

# admin.site.register(Review, ReviewAdmin)
