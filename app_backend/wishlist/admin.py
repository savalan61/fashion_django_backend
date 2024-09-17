# wishlist/admin.py

from django.contrib import admin
from .models import UserWishlist

class UserWishlistAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'user_id', 'favorite_products_list', 'created_at')
    search_fields = ('user__username',)  # امکان جستجو بر اساس نام کاربری
    list_filter = ('created_at',)  # امکان فیلتر بر اساس تاریخ

    def user_id(self, obj):
        return obj.user.id
    user_id.short_description = 'User ID'  # نام ستون در پنل مدیریت

    def favorite_products_list(self, obj):
        return ", ".join([str(product) for product in obj.favorite_products.all()])
    favorite_products_list.short_description = 'Favorite Products'  # نام ستون در پنل مدیریت

admin.site.register(UserWishlist, UserWishlistAdmin)
