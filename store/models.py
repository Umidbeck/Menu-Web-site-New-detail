from django.db import models

class Product(models.Model):
    """
    Product model to store information about restaurant menu items
    """
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    available = models.BooleanField(default=True)

    def __str__(self):
        """String representation of the Product model"""
        return self.name

class Cart(models.Model):
    """
    Cart model to store information about customer orders
    Uses a session key to track the cart for non-authenticated users
    """
    session_key = models.CharField(max_length=40)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """String representation of the Cart model"""
        return f"Cart {self.id} ({self.session_key})"
    
    def get_total_price(self):
        """Calculate total price of all cart items"""
        return sum(item.get_cost() for item in self.items.all())

class CartItem(models.Model):
    """
    CartItem model to store product quantities in a cart
    """
    cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='cart_items', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        """String representation of the CartItem model"""
        return f"{self.quantity} of {self.product.name}"
    
    def get_cost(self):
        """Calculate the cost of this cart item"""
        return self.product.price * self.quantity