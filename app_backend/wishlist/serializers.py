from rest_framework import serializers
from .models import UserWishlist
from .serializers import ProductModelSerializer

class UserWishlistSerializer(serializers.ModelSerializer):
    favorite_products = ProductModelSerializer(many=True, read_only=True)

    class Meta:
        model = UserWishlist
        fields = ['id', 'user', 'favorite_products', 'created_at']
