from rest_framework import generics, status
from rest_framework.response import Response
from . import models, serializers
from django.db.models import Count
import random

### ******************************************************** Get All Categories ******************************************************
class CategoryList(generics.ListAPIView):
    serializer_class = serializers.CategorySerializer
    queryset = models.CategoryModel.objects.all()

### ******************************************************** Get Random 5 Categories For HomePage ********************************************************
class HomeCategoryList(generics.ListAPIView):
    serializer_class = serializers.CategorySerializer

    def get_queryset(self):
        return models.CategoryModel.objects.order_by('?')[:5]

### ******************************************************** Get All Brands ******************************************************** 
class BrandList(generics.ListAPIView):
    serializer_class = serializers.BrandSerializer
    queryset = models.BrandModel.objects.all()

### ******************************************************** Get Random 20 Products ******************************************************** 
class ProductList(generics.ListAPIView):
    serializer_class = serializers.ProductSerializer

    def get_queryset(self):
        return models.ProductModel.objects.order_by('?')[:20]

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

### ******************************************************** Filter Prod By Category ******************************************************** 
class FilterProductsByCategory(generics.ListAPIView):
    serializer_class = serializers.ProductSerializer

    def get_queryset(self):
        # Retrieve the 'category' parameter from the query string
        category = self.request.query_params.get('category', None)
        
        if category:
            # Filter products based on the provided category
            queryset = models.ProductModel.objects.filter(category=category)
            return queryset
        else:
            # Return an empty queryset if 'category' parameter is not provided
            return models.ProductModel.objects.none()

    def get(self, request, *args, **kwargs):
        # Call get_queryset method to retrieve data
        queryset = self.get_queryset()
        # Use serializer to convert data to JSON format
        serializer = self.get_serializer(queryset, many=True)
        
        if queryset:
            return Response(serializer.data)
        else:
            return Response({'message': 'No products found for the provided category'}, status=status.HTTP_404_NOT_FOUND)

### ******************************************************** Add To  Category ******************************************************** 
class CategoryCreateView(generics.CreateAPIView):
    queryset = models.CategoryModel.objects.all()
    serializer_class = serializers.CategorySerializer



















# ***************************************************** Old code ***********************************
# ***************************************************** Old code ***********************************
# ***************************************************** Old code ***********************************
# ***************************************************** Old code ***********************************
# ***************************************************** Old code ***********************************
from rest_framework import generics, status
from . import models, serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Count
import random 

### ******************************************************** Get All Categories ******************************************************
# class CategoryList(generics.ListAPIView):
#     serializer_class = serializers.CategorySerializer
#     queryset = models.CategoryModel.objects.all()

# ### ******************************************************** Get Random 5 Categories For HomePage ********************************************************
# class HomeCategoryList(generics.ListAPIView):
#     serializer_class = serializers.CategorySerializer

#     def get_queryset(self):
#         queryset = models.CategoryModel.objects.all()
#         queryset = queryset.order_by('?')  # Random order
#         return queryset[:5]

# ###  ******************************************************** Get All Brands  ******************************************************** 
# class BrandList(generics.ListAPIView):
#     serializer_class = serializers.BrandSerializer
#     queryset = models.BrandModel.objects.all()

# ###  ******************************************************** Get Random 20 Products  ******************************************************** 
# class ProductList(generics.ListAPIView):
#     serializer_class = serializers.ProductSerializer

#     def get_queryset(self):
#         queryset = models.ProductModel.objects.all()
#         queryset = queryset.order_by('?')  # Random order
#         return queryset[:20]

# ###  ********************************************************  Get Popular Products  ******************************************************** 
# class PopularProductList(generics.ListAPIView):
#     serializer_class = serializers.ProductSerializer
    
#     def get_queryset(self):
#         queryset = models.ProductModel.objects.filter(rating__gte=4.0, rating__lte=5.0)
#         queryset = queryset.order_by('?')  # Random order
#         return queryset[:20]


###  ******************************************************** Get products By Type Of Clothes  ******************************************************** 
# class ProductListByClothesType(generics.ListAPIView):
#     serializer_class = serializers.ProductSerializer
    
#     def get_queryset(self, request):
#         query = request.query_params.get('clothesType', None)
#         if query: 
#             queryset = models.ProductModel.objects.filter(clothesType = query)
#             queryset = queryset.annotate(random_order = Count('id'))
#             products_list = list(queryset)
#             limited_products = products_list[:20]
#             serializer = serializers.ProductSerializer(limited_products, many = True)
#             return Response(serializer.data)
#         else:
#             return Response({'message':'No Query Provided'}, status=status.HTTP_400_BAD_REQUEST)


###  ********************************************************  For Test:Get products By Type Of Clothes  ******************************************************** 
# class ProductListByClothesType(generics.ListAPIView):
#     serializer_class = serializers.ProductSerializer

#     def get_queryset(self):
#         # Get 'clothesType' parameter from query string
#         clothes_type = self.request.query_params.get('clothesType', None)
        
#         if clothes_type:
#             # Filter products based on clothing type
#             queryset = models.ProductModel.objects.filter(clothesType=clothes_type)
#             # Add random order to products
#             queryset = queryset.annotate(random_order=Count('id'))
#             # Convert queryset to list and limit to 20 products
#             queryset = list(queryset)
#             return queryset[:20]
#         else:
#             # Return an empty queryset if 'clothesType' parameter is not provided
#             return models.ProductModel.objects.none()
    
#     def get(self, request, *args, **kwargs):
#         # Call get_queryset method to retrieve data
#         queryset = self.get_queryset()
#         # Use serializer to convert data to JSON format
#         serializer = self.get_serializer(queryset, many=True)
        
#         if queryset:
#             return Response(serializer.data)
#         else:
#             return Response({'message': 'No products found for the provided type'}, status=status.HTTP_404_NOT_FOUND)

# ###  ********************************************************  Similar Products  ******************************************************** 
# class SimilarProducts(APIView):
#     def get(self, request):
#         # Retrieve the 'category' parameter from the query string
#         category = request.query_params.get("category", None)

#         if category:
#             # Filter products by the provided category
#             products = models.ProductModel.objects.filter(category=category)
#             product_list = list(products)
            
#             # Shuffle the list of products randomly
#             random.shuffle(product_list)
            
#             # Limit the number of products to 6
#             limited_prod = product_list[:6]
            
#             # Serialize the limited product list into JSON format
#             serializer = serializers.ProductSerializer(limited_prod, many=True)
            
#             return Response(serializer.data)
#         else:
#             # Return an error message if the 'category' parameter is not provided
#             return Response({'message': 'No Query Provided'}, status=status.HTTP_400_BAD_REQUEST)

# ###  ********************************************************  Search Products  ******************************************************** 
# class SearchProductsByTitle(APIView):
#     def get(self, request):
#         # Retrieve the 'q' parameter from the query string
#         query = request.query_params.get('q', None)
        
#         if query:
#             # Filter products where the title contains the query string
#             products = models.ProductModel.objects.filter(title__icontains=query)
            
#             # Serialize the filtered products into JSON format
#             serializer = serializers.ProductSerializer(products, many=True)
            
#             return Response(serializer.data)
#         else:
#             # Return an error message if the 'q' parameter is not provided
#             return Response({'message': 'No Query Provided'}, status=status.HTTP_400_BAD_REQUEST)