from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import FavoriteList, ProductModel
from .serializers import FavoriteListSerializers

class FavoriteListView(generics.ListAPIView):
    serializer_class = FavoriteListSerializers
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return FavoriteList.objects.filter(user=self.request.user)


class ToggleFavoriteList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        product_id = request.query_params.get('id')

        if not product_id:
            return Response(
                {'message': 'Product id is required'},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            product = ProductModel.objects.get(id=product_id)
        except ProductModel.DoesNotExist:
            return Response(
                {'message': 'Product not found'},
                status=status.HTTP_404_NOT_FOUND
            )

        wishlist_item, created = FavoriteList.objects.get_or_create(user=request.user, product=product)

        if created:
            return Response(
                {'message': 'Product added to wish list'},
                status=status.HTTP_201_CREATED
            )
        else:
            wishlist_item.delete()
            return Response(
                {'message': 'Product removed from wish list'},
                status=status.HTTP_204_NO_CONTENT
            )
