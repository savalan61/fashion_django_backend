from django.shortcuts import render
from django.db import models
from .models import Cart, ProductModel
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response


class AddToCart(APIView):
    permission_classes = [IsAuthenticated]

    ### Add
    def post(self, request):
        user = request.user
        data = request.data

        try:
            product = ProductModel.objects.get(id=data['product'])
        except ProductModel.DoesNotExist:
            return Response({'message': 'Product does not exist'}, status=status.HTTP_404_NOT_FOUND)

        try:
            cart_item = Cart.objects.get(
                user=user,
                product=product,
                color=data['color'],
                size=data['size']
            )
            cart_item.quantity += data.get('quantity', 1)
            cart_item.save()
            return Response({'message': 'Cart updated successfully.'}, status=status.HTTP_200_OK)

        except Cart.DoesNotExist:
            cart_item = Cart.objects.create(
                user=user,
                product=product,
                color=data['color'],
                size=data['size'],
                quantity=data.get('quantity', 1)
            )
            cart_item.save()
            return Response({'message': 'Product added to cart successfully.'}, status=status.HTTP_201_CREATED)

    ### Remove
class RemoveItemFromCart(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, cart_item_id):
        user = request.user
        
        try:
            cart_item = Cart.objects.get(id=cart_item_id, user=user)
        except Cart.DoesNotExist:
            return Response({'message': 'Item not found in cart'}, status=status.HTTP_404_NOT_FOUND)

        cart_item.filter(id=cart_item_id).delete()
        return Response({'message': 'Item removed from cart successfully'}, status=status.HTTP_200_OK)


  ### Count Cart Count
class CartCount(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        cart_items_count = Cart.objects.filter(user=user).count()
        
        return Response({'cart_items_count': cart_items_count}, status=200)


# UpdateQuantity
class UpdateCartItemQuantity(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, cart_item_id):
        user = request.user
        new_quantity = request.data.get('quantity')

        if not new_quantity or int(new_quantity) <= 0:
            return Response({'message': 'Invalid quantity'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            cart_item = Cart.objects.get(id=cart_item_id, user=user)
        except Cart.DoesNotExist:
            return Response({'message': 'Cart item not found'}, status=status.HTTP_404_NOT_FOUND)

        cart_item.quantity = new_quantity
        cart_item.save()

        return Response({'message': 'Cart item quantity updated successfully'}, status=status.HTTP_200_OK)

    # 4:13