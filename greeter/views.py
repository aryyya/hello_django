from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

def help(request):
    return HttpResponseRedirect(reverse('greeter:greet', args=('user',), current_app=request.resolver_match.namespace))

def greet(request, name):
    return HttpResponse(f'Hello, {name}!')
