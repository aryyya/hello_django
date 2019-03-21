from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest, HttpResponseNotFound
from django.urls import reverse
from .models import Member
from django.core.exceptions import ObjectDoesNotExist

def help(request):
    return HttpResponseRedirect(reverse('greeter:greet', args=('user',), current_app=request.resolver_match.namespace))

def greet(request, name):
    return HttpResponse(f'Hello, {name}!')

def music(request):
    musician_query = request.GET.get('musician', '')
    band_query = request.GET.get('band', '')

    if musician_query == '' or band_query == '':
        return HttpResponseBadRequest('Error: Must provide query parameters "musician" and "band".')

    try:
        member = Member.objects.get(musician__name=musician_query, band__name=band_query)
    except ObjectDoesNotExist:
        return HttpResponseNotFound(f'Error: No information exists for {query["musician"]} from {query["band"]}.')

    musician = member.musician
    band = member.band

    return HttpResponse(f'{musician.name} played {musician.instrument} in the band {band.name}, which had {band.member_set.count() - 1} other members.')
