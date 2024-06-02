from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def module(request):
    return HttpResponse("this is Module_1")
