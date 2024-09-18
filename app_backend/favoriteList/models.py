from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from core.models import ProductModel 
class FavoriteList(models.Model):
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE)

    user = models.ForeignKey(User, on_delete= models.CASCADE)

    def __str__(self):
        return "{}/{}".format(self.user.username, self.product.title)


