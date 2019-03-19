from django.conf.urls import url, include
from django.contrib import admin
from django.http import HttpResponse
from django.urls import path

def index(request):
    return HttpResponse('hello_django says "Hello, world!"')

def greet(request, name):
    return HttpResponse(f'Hello, {name}!')

urlpatterns = [
    path('', index),
    path('greet/<str:name>', greet),
    path('admin/', admin.site.urls),
    url(r'^menu/', include('menu_api.urls')),
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework'))
]
