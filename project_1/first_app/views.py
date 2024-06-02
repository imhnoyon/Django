from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
 
def course(requst):
    return HttpResponse("This is courses pages")