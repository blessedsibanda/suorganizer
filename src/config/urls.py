from django.contrib import admin
from django.urls import path, include

api_urls = [
    path("", include("organizer.routers")),
    path("", include("blog.routers")),
]

urlpatterns = [
    path("admin/", admin.site.urls), 
    path('api/v1/', include(api_urls)),
    path('', include('organizer.urls')),
]
