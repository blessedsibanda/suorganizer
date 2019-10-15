import json

from django.views.decorators.http import require_http_methods
from rest_framework.generics import ListAPIView, RetrieveAPIView, \
                                        ListCreateAPIView,\
                                        RetrieveUpdateAPIView, \
                                        RetrieveUpdateDestroyAPIView
from django.shortcuts import get_object_or_404, redirect, render
from rest_framework.response import Response
from django.views.generic import ListView, DetailView, View
from django.urls import reverse
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_400_BAD_REQUEST,
)


from .models import Tag, Startup, NewsLink
from .forms import TagForm, StartupForm
from .serializers import TagSerializer, StartupSerializer, \
                            NewsLinkSerializer


class TagCreate(View):
    def get(self, request):
        context = {'form': TagForm(), 'update': False }
        return render(request, 'tag/form.html', context)

    def post(self, request):
        tform = TagForm(request.POST)
        if tform.is_valid():
            tag = tform.save()
            return redirect(tag.get_absolute_url())
        context = {'form': tform, 'update': False}
        return render(request, 'tag/form.html', context)

    
class TagUpdate(View):
    def get(self, request, slug):
        tag = get_object_or_404(Tag, slug=slug)
        context = {
            'tag': tag,
            'form': TagForm(instance=tag),
            'update': True,
        }
        return render(request, 'tag/form.html', context)

    def post(self, request, slug):
        tag = get_object_or_404(Tag, slug=slug)
        tform = TagForm(request.POST, instance=tag)
        if tform.is_valid():
            tag = tform.save()
            return redirect(tag.get_absolute_url())
        context = {'form': tform, 'update': True, 'tag': tag}
        return render(request, 'tag/form.html', context)


class TagDelete(View):
    def get(self, request, slug):
        tag = get_object_or_404(Tag, slug=slug)
        return render(
            request, 'tag/confirm_delete.html', {'tag': tag}
        )

    def post(self, request, slug):
        tag = get_object_or_404(Tag, slug=slug)
        tag.delete()
        return redirect(reverse('tag_list'))


class TagApiDetail(RetrieveUpdateDestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    lookup_field = 'slug'


class TagApiList(ListCreateAPIView):
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
    
    