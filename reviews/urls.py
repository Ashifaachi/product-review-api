from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_nested.routers import NestedDefaultRouter
from .views import (
    ProductViewSet, ReviewViewSet,
    RegisterView, LoginView, LogoutView, UserListView
)

# Main router for /products/
router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='products')

# Nested router for /products/<id>/reviews/
product_router = NestedDefaultRouter(router, r'products', lookup='product')
product_router.register(r'reviews', ReviewViewSet, basename='product-reviews')

# All URLs
urlpatterns = [
    path('', include(router.urls)),
    path('', include(product_router.urls)),

    # Auth endpoints
    path('auth/register/', RegisterView.as_view(), name='register'),
    path('auth/login/', LoginView.as_view(), name='login'),
    path('auth/logout/', LogoutView.as_view(), name='logout'),
    path('auth/users/', UserListView.as_view(), name='user-list'),
]
