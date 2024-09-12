from django.urls import path
from . import views

urlpatterns = [
    # URL for getting all categories
    path('categories/', views.CategoryList.as_view(), name='category-list'),
    
    # URL for getting random 5 categories for homepage
    path('home-categories/', views.HomeCategoryList.as_view(), name='home-category-list'),
    
    # URL for getting all brands
    path('brands/', views.BrandList.as_view(), name='brand-list'),
    
    # URL for getting random 20 products
    path('products/', views.ProductList.as_view(), name='product-list'),
    
    # URL for getting popular products
    path('popular-products/', views.PopularProductList.as_view(), name='popular-product-list'),
    
    # URL for getting products by type of clothes
    path('products-by-clothes-type/', views.ProductListByClothesType.as_view(), name='product-list-by-clothes-type'),
    
    # URL for getting similar products by category
    path('similar-products/', views.SimilarProducts.as_view(), name='similar-products'),
    
    # URL for searching products by title
    path('search-products/', views.SearchProductsByTitle.as_view(), name='search-products'),

    # URL for searching products by category
    path('filter-products-by-category/', views.FilterProductsByCategory.as_view(), name='filter-products-by-category'),

    #--------------------------------------------------------------------- Post -----------------------------------------------
    path('categories/create/', views.CategoryCreateView.as_view(), name='category-create'),
]
