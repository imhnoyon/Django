from django.shortcuts import render,redirect
from . import forms
# Create your views here.
def AddProfile(request):
    if request.method=='POST':
        profile=forms.ProfileForm(request.POST)
        if profile.is_valid():
            profile.save()
            print(profile)
            return redirect("AddProfile")

    else:
         profile=forms.ProfileForm()
    return render(request,'add_profile.html',{'form':profile})