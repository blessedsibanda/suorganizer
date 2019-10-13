from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from django.views import View


class HelloWorld(View):
    def get(self, request):
        return HttpResponse("Hello blessed world!")    

