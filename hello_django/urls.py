from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

def index(request):
    return HttpResponse('hello_django says: "Hello, world!"')

urlpatterns = [
    path('', index),
    path('admin/', admin.site.urls),
    url(r'^menu/', include('menu_api.urls')),
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework'))
]
