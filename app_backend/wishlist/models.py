# wishlist/models.py

# wishlist/models.py

from django.db import models
from django.contrib.auth.models import User
from core.models import ProductModel  # مطمئن شوید که import درست است

class UserWishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    favorite_products = models.ManyToManyField(ProductModel, related_name='favorited_by')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Wishlist of {self.user.username}"

    class Meta:
        verbose_name = "User Wishlist"
        verbose_name_plural = "User Wishlists"
