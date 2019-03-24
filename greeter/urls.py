from . import views
from django.urls import path

app_name = 'greeter'

urlpatterns = [
    path('help', views.help),
    path('music', views.music, name='music'),
    path('band', views.band_list, name='band-list'),
    path('band/<str:band>', views.band_info, name='band-info')
]
