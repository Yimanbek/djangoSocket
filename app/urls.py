from django.urls import path, include
from rest_framework.routers import DefaultRouter
from app.views import (
    ProfileViewSet, CategoryViewSet, ProductViewSet, TagViewSet
)

router = DefaultRouter()
router.register(r'profiles', ProfileViewSet, basename='profile')
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'products', ProductViewSet, basename='product')
router.register(r'tags', TagViewSet, basename='tag')

urlpatterns = [
    path('', include(router.urls)),
]
