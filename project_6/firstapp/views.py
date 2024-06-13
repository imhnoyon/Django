from django.shortcuts import render, redirect
from . import models
# Create your views here.
def home(request):
    infor=models.Student.objects.all()
    return render(request,'home.html',{'data':infor})


def delete_student(request,roll):
    std=models.Student.objects.get(pk=roll).delete()
    print(std)
    return redirect("homepages")
     