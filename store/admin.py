from django.contrib import admin
from .models import Product, Cart, CartItem

class CartItemInline(admin.TabularInline):
    """
    Inline admin for displaying cart items within the cart admin
    """
    model = CartItem
    extra = 0  # No extra empty forms

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Product model
    """
    list_display = ['name', 'price', 'available', 'created_at']
    list_filter = ['available', 'created_at']
    search_fields = ['name', 'description']
    list_editable = ['price', 'available']
    readonly_fields = ['created_at', 'updated_at']
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'description', 'price', 'image')
        }),
        ('Status', {
            'fields': ('available', 'created_at', 'updated_at')
        }),
    )

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Cart model
    """
    list_display = ['id', 'session_key', 'created_at', 'item_count', 'total_price']
    list_filter = ['created_at']
    search_fields = ['session_key']
    inlines = [CartItemInline]
    
    def item_count(self, obj):
        """Show the number of items in the cart"""
        return obj.items.count()
    
    def total_price(self, obj):
        """Show the total price of the cart"""
        return obj.get_total_price()

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    """
    Admin configuration for the CartItem model
    """
    list_display = ['id', 'cart', 'product', 'quantity']
    list_filter = ['cart']
    search_fields = ['product__name']