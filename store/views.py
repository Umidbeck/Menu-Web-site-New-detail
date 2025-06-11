from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .models import Product, Cart, CartItem

def get_cart(request):
    """
    Helper function to get or create a cart based on the session
    """
    session_key = request.session.session_key
    if not session_key:
        request.session.create()
        session_key = request.session.session_key
    
    cart, created = Cart.objects.get_or_create(session_key=session_key)
    return cart

def product_list(request):
    """
    View to display all available products
    """
    products = Product.objects.filter(available=True)
    cart = get_cart(request)
    cart_items_count = cart.items.count()
    
    return render(request, 'store/index.html', {
        'products': products,
        'cart_items_count': cart_items_count
    })

def product_detail(request, product_id):
    """
    View to display details of a specific product
    """
    product = get_object_or_404(Product, id=product_id, available=True)
    cart = get_cart(request)
    cart_items_count = cart.items.count()
    
    return render(request, 'store/product_detail.html', {
        'product': product,
        'cart_items_count': cart_items_count
    })

@require_POST
def add_to_cart(request, product_id):
    """
    View to add a product to the cart
    """
    product = get_object_or_404(Product, id=product_id)
    cart = get_cart(request)
    
    # Get quantity from form, default to 1
    quantity = int(request.POST.get('quantity', 1))
    
    # Check if the product is already in the cart
    cart_item, created = CartItem.objects.get_or_create(
        cart=cart,
        product=product,
        defaults={'quantity': quantity}
    )
    
    # If the product was already in the cart, update the quantity
    if not created:
        cart_item.quantity += quantity
        cart_item.save()
    
    return redirect('cart')

def cart_view(request):
    """
    View to display the cart contents
    """
    cart = get_cart(request)
    cart_items = cart.items.all()
    total = cart.get_total_price()
    
    return render(request, 'store/cart.html', {
        'cart_items': cart_items,
        'total': total,
        'cart_items_count': cart_items.count()
    })

@require_POST
def update_cart(request, item_id):
    """
    View to update the quantity of a cart item
    """
    cart_item = get_object_or_404(CartItem, id=item_id)
    
    # Get quantity from form
    quantity = int(request.POST.get('quantity', 1))
    
    if quantity > 0:
        cart_item.quantity = quantity
        cart_item.save()
    else:
        cart_item.delete()
    
    return redirect('cart')

@require_POST
def remove_from_cart(request, item_id):
    """
    View to remove a product from the cart
    """
    cart_item = get_object_or_404(CartItem, id=item_id)
    cart_item.delete()
    
    return redirect('cart')

def clear_cart(request):
    """
    View to clear the cart
    """
    cart = get_cart(request)
    cart.items.all().delete()
    
    return redirect('cart')