from . import views
from django.urls import path

app_name = 'greeter'

urlpatterns = [
    path('help', views.help),
    path('music', views.music, name='music'),
    path('<str:name>', views.greet, name='greet')
]
