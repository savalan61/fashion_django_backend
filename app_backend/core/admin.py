from django.contrib import admin
from .models import BrandModelAdmin, CategoryModel, BrandModel, ProductModel, CategoryModelAdmin, ProductModelAdmin
from django.utils.html import format_html

admin.site.register(CategoryModel, CategoryModelAdmin)
admin.site.register(BrandModel, BrandModelAdmin)
admin.site.register(ProductModel, ProductModelAdmin)
