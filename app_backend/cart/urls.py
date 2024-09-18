from django.urls import path
from .views import AddToCart, RemoveItemFromCart

urlpatterns = [
    path('cart/add/', AddToCart.as_view(), name='add_to_cart'),
    path('cart/remove/<int:cart_item_id>/', RemoveItemFromCart.as_view(), name='remove_item_from_cart'),
]
