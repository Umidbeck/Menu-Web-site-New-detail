#!/usr/bin/env python
import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'restaurant_project.settings')
django.setup()

from store.models import Product
from decimal import Decimal

def add_sample_products():
    """
    Adds sample restaurant products to the database if they don't already exist.
    """
    # Check if we already have products
    if Product.objects.count() > 0:
        print("Products already exist in the database.")
        return

    # Sample restaurant products
    products = [
        {
            'name': 'Margherita Pizza',
            'description': 'Classic pizza with tomato sauce, mozzarella, fresh basil, salt, and extra-virgin olive oil.',
            'price': Decimal('12.99'),
            'available': True,
        },
        {
            'name': 'Spaghetti Carbonara',
            'description': 'Traditional Italian pasta dish with eggs, cheese, pancetta, and black pepper.',
            'price': Decimal('14.50'),
            'available': True,
        },
        {
            'name': 'Caesar Salad',
            'description': 'Fresh romaine lettuce with Caesar dressing, croutons, and parmesan cheese.',
            'price': Decimal('8.99'),
            'available': True,
        },
        {
            'name': 'Beef Burger',
            'description': 'Juicy beef patty with lettuce, tomato, onions, and special sauce, served with fries.',
            'price': Decimal('15.99'),
            'available': True,
        },
        {
            'name': 'Chocolate Lava Cake',
            'description': 'Warm chocolate cake with a melting chocolate center, served with vanilla ice cream.',
            'price': Decimal('7.50'),
            'available': True,
        },
    ]

    # Create products
    for product_data in products:
        Product.objects.create(**product_data)
        print(f"Added product: {product_data['name']}")

    print(f"Successfully added {len(products)} sample products to the database.")

if __name__ == "__main__":
    add_sample_products()