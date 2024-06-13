from django.shortcuts import render, redirect
from . import models
from . import forms
# Create your views here.
def home(request):
    infor=models.Student.objects.all()
    return render(request,'home.html',{'data':infor})


def delete_student(request,roll):
    std=models.Student.objects.get(pk=roll).delete()
    print(std)
    return redirect("homepages")
     

def home2(request):
    if request.method=="POST":
        form=forms.StudentForm(request.POST)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)

    else:
        form=forms.StudentForm()
    return render(request,'home2.html',{'form':form})