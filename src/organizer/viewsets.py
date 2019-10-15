from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_201_CREATED,
    HTTP_204_NO_CONTENT,
    HTTP_400_BAD_REQUEST
)
from rest_framework.viewsets import ModelViewSet

from .models import Tag 
from .serializers import TagSerializer


class TagViewSet(ModelViewSet): 
    lookup_field = 'slug'
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    