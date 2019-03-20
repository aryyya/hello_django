from . import converters
from . import views
from django.conf.urls import url, include
from django.contrib import admin
from django.http import HttpResponse
from django.urls import path, register_converter

app_name = 'hello_django'

register_converter(converters.YearConverter, 'yyyy')

urlpatterns = [
    path('', views.index, name='root'),
    path('greet/<str:name>/', views.greet),
    path('get-age/<yyyy:birth_year>/', views.get_age),
    path('standard-greeter/', include('greeter.urls', namespace='standard-greeter')),
    path('special-greeter/', include('greeter.urls', namespace='special-greeter')),
    path('user/<str:name>/', include([
        path('', views.user_name),
        path('greet/', views.user_greet)
    ])),
    path('admin/', admin.site.urls),
    url(r'^menu/', include('menu_api.urls')),
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),
]
