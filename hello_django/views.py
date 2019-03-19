from datetime import datetime
from django.http import HttpResponse

def index(request):
    return HttpResponse('hello_django says "Hello, world!"', content_type='text/plain')

def greet(request, name):
    return HttpResponse(f'Hello, {name}!', content_type='text/plain')

def get_age(request, birth_year):
    age = datetime.now().year - birth_year
    return HttpResponse( f'You are {age} years old.', content_type='text/plain',)
