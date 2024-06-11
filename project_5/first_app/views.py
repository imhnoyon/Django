from django.shortcuts import render
from . import forms
# Create your views here.

def form(request):
    return render(request,'form.html')
 


def about(request):
    if request.method=='POST':
        name= request.POST.get('userName')
        email=request.POST.get('userEmail')
        selects=request.POST.get('select')
        return render(request,'about.html',{'name':name, 'email':email,'selects':selects})
    else:
        return render(request,'about.html')
    

def django_form(request):
    if request.method=="POST":
        form=forms.contactForm()  # contact form er parameter (request.POST,request.FILES)
        if form.is_valid():
            # file=form.cleaned_data['file']
            # with open("./first_app/upload/" + file.name, 'wb+') as destination:
            #     for chunk in file.chunks():
            #         destination.write(chunk)
            print(form.cleaned_data)
            # return render(request,'django_form.html',{'form':form})
    else:
        form=forms.contactForm()
    return render(request,'django_form.html',{'form':form})


def student(request):
     if request.method=="POST":
        form=forms.studentForm(request.POST,request.FILES) 
        if form.is_valid():
            print(form.cleaned_data)
    
     else:
        form=forms.studentForm()
     return render(request,'student_form.html',{'form':form})


def passwordvalid(request):
     if request.method=="POST":
        form=forms.passwordValidation(request.POST) 
        if form.is_valid():
            print(form.cleaned_data)
    
     else:
        form=forms.passwordValidation()
     return render(request,'password.html',{'form':form})



                       
   







