# views.py

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from . import models

class ToggleWishes(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        product_id = request.data.get('id')  # استفاده از request.data برای POST

        if not product_id:
            return Response({'message': 'Product id is required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            product = models.ProductModel.objects.get(id=product_id)
        except models.ProductModel.DoesNotExist:
            return Response({'message': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)

        # Get or create a UserWishlist for the user
        wish_list, created = models.UserWishlist.objects.get_or_create(user=user)

        # Add or remove the product from the wish list
        if product in wish_list.favorite_products.all():
            wish_list.favorite_products.remove(product)
            return Response({'message': 'Product removed from wish list'}, status=status.HTTP_200_OK)
        else:
            wish_list.favorite_products.add(product)
            return Response({'message': 'Product added to wish list'}, status=status.HTTP_200_OK)
