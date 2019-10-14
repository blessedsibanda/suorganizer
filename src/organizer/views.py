import json

from django.views.decorators.http import require_http_methods
from rest_framework.response import Response 
from rest_framework.generics import ListAPIView, RetrieveAPIView
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView

from .models import Tag, Startup, NewsLink
from .serializers import TagSerializer, StartupSerializer, \
                            NewsLinkSerializer


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


class NewsLinkAPIDetail(RetrieveAPIView):
    queryset = NewsLink.objects.all()
    serializer_class = NewsLinkSerializer

    def get_object(self):
        startup_slug = self.kwargs.get('startup_slug')
        newslink_slug = self.kwargs.get('newslink_slug')

        queryset = self.filter_queryset(self.get_queryset())

        newslink = get_object_or_404(
            queryset,
            slug=newslink_slug,
            startup__slug=startup_slug
        )  
        self.check_object_permissions(self.request, newslink)
        return newslink


class NewsLinkAPIList(ListAPIView):
    queryset = NewsLink.objects.all()
    serializer_class = NewsLinkSerializer


class TagList(ListView):
    model = Tag 
    context_object_name = 'tag_list'
    template_name = 'tag/list.html'


class TagDetail(DetailView):
    model = Tag 
    context_object_name = 'tag'
    template_name = 'tag/detail.html'

class StartupDetail(DetailView):
    template_name = 'startup/detail.html'
    queryset = Startup.objects.all()
    context_object_name = 'startup'

class StartupList(ListView):
    template_name = 'startup/list.html'
    queryset = Startup.objects.all()
    context_object_name = 'startup_list'
    
    