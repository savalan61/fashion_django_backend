from django.db import models
from django.contrib.auth.models import User
from core.models import ProductModel
from django.utils import timezone


# Create your models here.
class Cart(models.Model):
    user =models.ForeignKey(User, on_delete=models.CASCADE)
    product =  models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    size = models.CharField(max_length=20, blank=False)
    color = models.CharField(max_length=20, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        
        return f'{self.user.username} - {self.product.title} (Quantity: {self.quantity} - Size: {self.size} - Color: {self.color})'
