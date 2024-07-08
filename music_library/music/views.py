from django.shortcuts import render
from django.http import HttpResponse


def artist(request):
    return HttpResponse('Artist')


def album(request):
    return HttpResponse('Album')


def song(request):
    return HttpResponse('Song')
# Create your views here.
