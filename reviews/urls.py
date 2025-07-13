from django.urls import path, include
from rest_framework.routers import SimpleRouter
from rest_framework_nested.routers import NestedSimpleRouter

from .views import (
    ProductViewSet, ReviewViewSet,
    RegisterView, LoginView, LogoutView, UserListView
)

# Use SimpleRouter instead of DefaultRouter
router = SimpleRouter()
router.register(r'products', ProductViewSet, basename='products')

# Nested router for /products/<id>/reviews/
product_router = NestedSimpleRouter(router, r'products', lookup='product')
product_router.register(r'reviews', ReviewViewSet, basename='product-reviews')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(product_router.urls)),

    # Auth endpoints
    path('auth/register/', RegisterView.as_view(), name='register'),
    path('auth/login/', LoginView.as_view(), name='login'),
    path('auth/logout/', LogoutView.as_view(), name='logout'),
    path('auth/users/', UserListView.as_view(), name='user-list'),
]
