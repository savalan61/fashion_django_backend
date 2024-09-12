from django.contrib import admin
from .models import CategoryModel, BrandModel, ProductModel
from django.utils.html import format_html

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

admin.site.register(CategoryModel, CategoryModelAdmin)
admin.site.register(BrandModel, BrandModelAdmin)
admin.site.register(ProductModel, ProductModelAdmin)
