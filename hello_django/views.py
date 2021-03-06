from datetime import datetime
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def greet(request, name):
    return HttpResponse(f'Hello, {name}!', content_type='text/plain')

def get_age(request, birth_year):
    age = datetime.now().year - birth_year
    return HttpResponse( f'You are {age} years old.', content_type='text/plain',)

def user_name(request, name):
    return HttpResponse(f'name: {name}', content_type='text/plain')

def user_greet(request, name):
    return greet(request, name)
