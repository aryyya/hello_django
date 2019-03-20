from . import views
from django.urls import path

app_name = 'greeter'

urlpatterns = [
    path('help', views.help),
    path('<str:name>', views.greet, name='greet')
]
