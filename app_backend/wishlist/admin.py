from django.contrib import admin

# Register your models here.
from django.contrib import admin
from . models import  UserWishlist



# @admin.register(UserWishlist)
# class UserWishlistAdmin(admin.ModelAdmin):
#     list_display = ('user', 'created_at')
admin.site.register(UserWishlist)