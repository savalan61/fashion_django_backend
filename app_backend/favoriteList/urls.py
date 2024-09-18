from django.urls import path
from .views import FavoriteListView, ToggleFavoriteList

urlpatterns = [
    path('me/', FavoriteListView.as_view(), name='user_wishlist'),
    path('toggle/', ToggleFavoriteList.as_view(), name='toggle_favorite'),
]
