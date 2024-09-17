from rest_framework import serializers
from .models import UserWishlist

class WishListSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        from core.models import ProductModel  
        super().__init__(*args, **kwargs)

    id = serializers.ReadOnlyField(source='favorite_products.id')
    title = serializers.ReadOnlyField(source='favorite_products.title')
    price = serializers.ReadOnlyField(source='favorite_products.price')
    description = serializers.ReadOnlyField(source='favorite_products.description')
    isFeatured = serializers.ReadOnlyField(source='favorite_products.isFeatured')
    clothesType = serializers.ReadOnlyField(source='favorite_products.clothesType')
    rating = serializers.ReadOnlyField(source='favorite_products.rating')
    category = serializers.PrimaryKeyRelatedField(read_only=True, source='favorite_products.category')
    brand = serializers.PrimaryKeyRelatedField(read_only=True, source='favorite_products.brand')
    colors = serializers.ReadOnlyField(source='favorite_products.colors')
    sizes = serializers.ReadOnlyField(source='favorite_products.sizes')
    imageUrls = serializers.ReadOnlyField(source='favorite_products.imageUrls')
    created_at = serializers.ReadOnlyField(source='favorite_products.created_at')

    class Meta:
        model = UserWishlist
        fields = [
            'id', 'title', 'price', 'description',
            'isFeatured', 'clothesType', 'rating',
            'category', 'brand', 'colors', 
            'sizes', 'imageUrls', 'created_at'
        ]
