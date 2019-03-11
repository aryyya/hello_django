from django.shortcuts import render
from django.http import HttpResponse

def items(request):
    return HttpResponse('Hello, world!')
