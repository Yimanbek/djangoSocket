from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Profile, Category, Product, Tag
from .serializers import (
    ProfileSerializer, CategorySerializer,
    ProductSerializer, TagSerializer
)
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

class ProfileViewSet(ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        instance = serializer.save()
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "notify_group",
            {
                "type": "send_notification",
                "text": {
                    "message": f"New product created: {instance.name}, category: {instance.category}"
                }
            }
        )

class TagViewSet(ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer




def index(request):
    return render(request, 'index.html')

