from django.urls import path
from . import views

urlpatterns = [
    # Homepage with product list
    path('', views.product_list, name='product_list'),
    
    # Product detail page
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    
    # Cart related URLs
    path('cart/', views.cart_view, name='cart'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('update-cart/<int:item_id>/', views.update_cart, name='update_cart'),
    path('remove-from-cart/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('clear-cart/', views.clear_cart, name='clear_cart'),
]