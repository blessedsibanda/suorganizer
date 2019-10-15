from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.status import (
    HTTP_201_CREATED,
    HTTP_204_NO_CONTENT,
    HTTP_400_BAD_REQUEST
)
from rest_framework.viewsets import ModelViewSet

from .models import Tag, Startup
from .serializers import TagSerializer, StartupSerializer


class TagViewSet(ModelViewSet): 
    lookup_field = 'slug'
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    
class StartupViewSet(ModelViewSet): 
    lookup_field = 'slug'
    queryset = Startup.objects.all()
    serializer_class = StartupSerializer

    @action(detail=True, methods=['HEAD', 'GET', 'POST'])
    def tags(self, request, slug=None):
        startup = self.get_object()
        if request.method in ('HEAD', 'GET'):
            s_tag = TagSerializer(
                startup.tags,
                many=True,
                context={'request': request}
            )
            return Response(s_tag.data)
        tag_slug = request.data.get('slug')
        if not tag_slug:
            return Response(
                'Slug of a Tag must be specified',
                status=HTTP_400_BAD_REQUEST,
            )
        tag = get_object_or_404(Tag, slug__iexact=tag_slug)
        startup.tags.add(tag)
        return Response(status=HTTP_204_NO_CONTENT)