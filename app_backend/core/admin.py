from django.contrib import admin
from .models import CategoryModel, BrandModel, ProductModel
from django.utils.html import format_html

class CategoryModelAdmin(admin.ModelAdmin):
    # Display title and image in the table
    list_display = ('title', 'image_tag')
    
    def image_tag(self, obj):
        # Display image as HTML tag in the table
        if obj.imageUrl:
            return format_html('<img src="{}" width="100" height="100" />', obj.imageUrl)
        return '-'
    image_tag.short_description = 'Image'  # Change column title to 'Image'

class BrandModelAdmin(admin.ModelAdmin):
    # Display title and image in the table
    list_display = ('title', 'image_tag')
    
    def image_tag(self, obj):
        # Display image as HTML tag in the table
        if obj.imageUrl:
            return format_html('<img src="{}" width="100" height="100" />', obj.imageUrl)
        return '-'
    image_tag.short_description = 'Image'  # Change column title to 'Image'

class ProductModelAdmin(admin.ModelAdmin):
    # Display title, price, rating, category, and brand in the table
    list_display = ('title', 'price', 'rating', 'category', 'brand')

# Register models with custom settings
admin.site.register(CategoryModel, CategoryModelAdmin)
admin.site.register(BrandModel, BrandModelAdmin)
admin.site.register(ProductModel, ProductModelAdmin)
