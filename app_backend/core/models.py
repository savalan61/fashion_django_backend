from django.utils import timezone
from django.db import models
from django.contrib import admin
from django.utils.html import format_html


class CategoryModel(models.Model):
    title = models.CharField(max_length=255, unique=True)  
    imageUrl = models.URLField(max_length=500, blank=False)
      
    def __str__(self):
        return self.title 

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

class BrandModel(models.Model):
    title = models.CharField(max_length=255, unique=True)  
    imageUrl = models.URLField(max_length=500, blank=False)
      
    def __str__(self):
        return self.title 

    class Meta:
        verbose_name = "Brand"
        verbose_name_plural = "Brands"

class ProductModel(models.Model):
    title = models.CharField(max_length=255)  
    price = models.FloatField(default=0, blank=False)
    description = models.TextField(max_length=550)
    isFeatured = models.BooleanField(default=False)
    clothesType = models.CharField(max_length=255, default="unisex")
    rating = models.FloatField(blank=False, default=1.0)
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE)
    brand = models.ForeignKey(BrandModel, on_delete=models.CASCADE)
    colors = models.JSONField(blank=True)
    sizes = models.JSONField(blank=True)
    imageUrls = models.JSONField(blank=True)
    created_at = models.DateTimeField(default=timezone.now, blank=False)
      
    def __str__(self):
        return self.title 

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"



# ------------------------ Admin Panel Models --------------------------------------
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'image_tag')
    
    def image_tag(self, obj):
        if obj.imageUrl:
            return format_html('<img src="{}" width="100" height="100" />', obj.imageUrl)
        return '-'
    image_tag.short_description = 'Image'

class BrandModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'image_tag')
    
    def image_tag(self, obj):
        if obj.imageUrl:
            return format_html('<img src="{}" width="100" height="100" />', obj.imageUrl)
        return '-'
    image_tag.short_description = 'Image'

class ProductModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'rating', 'category', 'brand')


