
from django.shortcuts import render

def base(request):
    return render(request,'base.html')


def Home(request):
    return render(request,'home.html')