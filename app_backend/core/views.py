from rest_framework import generics, status
from rest_framework.response import Response
from . import models, serializers
import random

# **************************************************** Category Views ****************************************************

### ******************************************************** Get All Categories ******************************************************

class CategoryList(generics.ListAPIView):
    serializer_class = serializers.CategorySerializer
    queryset = models.CategoryModel.objects.all()

### ******************************************************** Get Random 5 Categories For HomePage ********************************************************
class HomeCategoryList(generics.ListAPIView):
    serializer_class = serializers.CategorySerializer

    def get_queryset(self):
        return models.CategoryModel.objects.order_by('?')[:5]

### ******************************************************** Create A New Category ********************************************************
class CategoryCreateView(generics.CreateAPIView):
    serializer_class = serializers.CategorySerializer

# **************************************************** Product Views ****************************************************

### ******************************************************** Get Random 20 Products ********************************************************
class ProductList(generics.ListAPIView):
    serializer_class = serializers.ProductSerializer

    def get_queryset(self):
        return models.ProductModel.objects.order_by('?')[:20]

### ******************************************************** Create A New Product ********************************************************
class ProductCreateView(generics.CreateAPIView):
    serializer_class = serializers.ProductSerializer

### ******************************************************** Get Popular Products ********************************************************
class PopularProductList(generics.ListAPIView):
    serializer_class = serializers.ProductSerializer

    def get_queryset(self):
        return models.ProductModel.objects.filter(rating__gte=4.0, rating__lte=5.0).order_by('?')[:20]

### ******************************************************** Get Products By Type Of Clothes ********************************************************

class ProductListByClothesType(generics.ListAPIView):
    serializer_class = serializers.ProductSerializer

    def get_queryset(self):
        clothes_type = self.request.query_params.get('clothesType', None)
        if clothes_type:
            return models.ProductModel.objects.filter(clothesType=clothes_type).order_by('?')[:20]
        return models.ProductModel.objects.none()

### ******************************************************** Similar Products ********************************************************
class SimilarProducts(generics.ListAPIView):
    serializer_class = serializers.ProductSerializer

    def get_queryset(self):
        category = self.request.query_params.get("category", None)
        if category:
            queryset = models.ProductModel.objects.filter(category=category)
            queryset = list(queryset)
            random.shuffle(queryset)
            return queryset[:6]
        return models.ProductModel.objects.none()

### ******************************************************** Search Products ********************************************************
class SearchProductsByTitle(generics.ListAPIView):
    serializer_class = serializers.ProductSerializer

    def get_queryset(self):
        query = self.request.query_params.get('q', None)
        if query:
            return models.ProductModel.objects.filter(title__icontains=query)
        return models.ProductModel.objects.none()

### ******************************************************** Get Product By Category ********************************************************
class FilterProductsByCategory(generics.ListAPIView):
    serializer_class = serializers.ProductSerializer

    def get_queryset(self):
        category = self.request.query_params.get('category', None)
        if category:
            return models.ProductModel.objects.filter(category=category)
        return models.ProductModel.objects.none()

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        if queryset:
            return Response(serializer.data)
        else:
            return Response({'message': 'No products found for the provided category'}, status=status.HTTP_404_NOT_FOUND)

# **************************************************** Brand Views ****************************************************

### ******************************************************** Get All Brands ********************************************************
class BrandList(generics.ListAPIView):
    serializer_class = serializers.BrandSerializer
    queryset = models.BrandModel.objects.all()

### ******************************************************** Create New Brand ********************************************************
class BrandCreateView(generics.CreateAPIView):
    serializer_class = serializers.BrandSerializer
