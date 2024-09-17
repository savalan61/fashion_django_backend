from . import models
from core.models import ProductModel

from django.contrib.auth.models import User
class WishList(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_products = models.ManyToManyField(ProductModel, related_name='favorited_by')

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = "User WishList"
        verbose_name_plural = "User WishLists"
