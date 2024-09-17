from rest_framework import serializers
from . models import WishList

class WishListSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField(source='product.id')
    title = serializers.ReadOnlyField(source='product.title')
    price = serializers.ReadOnlyField(source='product.price')
    description = serializers.ReadOnlyField(source='product.description')
    isFeatured = serializers.ReadOnlyField(source='product.isFeatured')
    clothesType = serializers.ReadOnlyField(source='product.clothesType')
    rating = serializers.ReadOnlyField(source='product.rating')
    category = serializers.PrimaryKeyRelatedField(read_only=True, source='product.category')
    brand = serializers.PrimaryKeyRelatedField(read_only=True, source='product.brand')
    colors = serializers.ReadOnlyField(source='product.colors')
    sizes = serializers.ReadOnlyField(source='product.sizes')
    imageUrls = serializers.ReadOnlyField(source='product.imageUrls')
    created_at = serializers.ReadOnlyField(source='product.created_at')

    class Meta:
        model = WishList
        fields = [
            'id', 'title', 'price', 'description',
            'isFeatured', 'clothesType', 'rating',
            'category', 'brand', 'colors', 
            'sizes', 'imageUrls', 'created_at'
        ]
