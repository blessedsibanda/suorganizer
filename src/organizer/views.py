import json

from django.views.decorators.http import require_http_methods
from rest_framework.response import Response 
from rest_framework.generics import ListAPIView, RetrieveAPIView

from .models import Tag, Startup
from .serializers import TagSerializer, StartupSerializer


class TagApiDetail(RetrieveAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    lookup_field = 'slug'


class TagApiList(ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class StartupAPIDetail(RetrieveAPIView):
    queryset = Startup.objects.all()
    serializer_class = StartupSerializer
    lookup_field = 'slug'


class StartupAPIList(ListAPIView):
    queryset = Startup.objects.all()
    serializer_class = StartupSerializer