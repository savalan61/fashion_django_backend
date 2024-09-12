from rest_framework import serializers
from . import models

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CategoryModel
        fields = ('id', 'title','imageUrl' )

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BrandModel
        fields = ('id', 'title', 'imageUrl')


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProductModel
        fields = '__all__'

# class ProductSerializer(serializers.ModelSerializer):
#     category = CategorySerializer()
#     brand = BrandSerializer()

#     class Meta:
#         model = models.ProductModel
#         fields = '__all__'
