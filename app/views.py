from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def radha(request,name):
    return HttpResponse(f'welcome to hai {name}')