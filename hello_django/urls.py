from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^menu/', include('menu_api.urls')),
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework'))
]
