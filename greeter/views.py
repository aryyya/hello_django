from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest, HttpResponseNotFound
from django.urls import reverse
from .models import Member, Band, Musician
from django.core.exceptions import ObjectDoesNotExist

def help(request):
    return HttpResponseRedirect(reverse('greeter:greet', args=('user',), current_app=request.resolver_match.namespace))

def music(request):
    musician_query = request.GET.get('musician', '')
    band_query = request.GET.get('band', '')

    if musician_query == '':
        return HttpResponseBadRequest('Error: Must provide query parameter "musician".')
    if band_query == '':
        return HttpResponseBadRequest('Error: Must provide query parameter "band".')

    try:
        member = Member.objects.get(musician__name__iexact=musician_query, band__name__iexact=band_query)
    except ObjectDoesNotExist:
        return HttpResponseNotFound(f'Error: No information exists for {musician_query} from {band_query}.')

    musician = member.musician
    band = member.band

    return HttpResponse(f'{musician.name} played {musician.instrument} in the band {band.name}, which had {band.member_set.count() - 1} other members.')

def band_list(request):
    bands = Band.objects.all()

    band_names = []
    for band in bands:
        band_names.append(f'<li><a href="band/{band.name}">{band.name}</a></li>')
    band_names = "".join(band_names)

    return HttpResponse(f'<ul>{band_names}</ul>')

def band_info(request, band):
    try:
        band = Band.objects.get(name__iexact=band)
    except ObjectDoesNotExist:
        return HttpResponseNotFound(f'Error, no information exists for {band}.')

    musicians = Musician.objects.filter(member__band=band)
    if len(musicians) == 0:
        return HttpResponseNotFound(f'Error, there are no members in {band}.')

    musician_names = []
    for musician in musicians:
        musician_names.append(musician.name)
    musician_names = ', '.join(musician_names)

    return HttpResponse(f'\
      <div>Band: {band.name}</div>\
      <div>Members: {musician_names}</div>\
    ')
