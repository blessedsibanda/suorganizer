import json

from django.views.decorators.http import require_http_methods
from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework.response import Response 
from rest_framework.views import APIView

from .models import Tag, Startup
from .serializers import TagSerializer, StartupSerializer


class TagApiDetail(APIView):
    def get(self, request, slug):
        tag = get_object_or_404(Tag, slug=slug)
        s_tag = TagSerializer(
            tag,
            context={'request': request}
        )
        return Response(s_tag.data)    


class TagApiList(APIView):
    def get(self, request):
        tag_list = get_list_or_404(Tag)
        s_tags = TagSerializer(
            tag_list, many=True,
            context={'request': request}
        )
        return Response(s_tags.data)


class StartupAPIDetail(APIView):
    def get(self, request, slug):
        startup = get_object_or_404(Startup, slug=slug)
        s_startup = StartupSerializer(
            startup,
            context={ 'request': request }
        )
        return Response(s_startup.data)


class StartupAPIList(APIView):
    def get(self, request):
        startup_list = get_list_or_404(Startup)
        s_startup = StartupSerializer(
            startup_list,
            many=True,
            context = {'request': request }
        )
        return Response(s_startup.data)