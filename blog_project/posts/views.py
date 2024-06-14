from django.shortcuts import render, redirect
from . import forms
# Create your views here.
def add_post(request):
    if request.method=='POST':
        post=forms.PostForm(request.POST)
        if post.is_valid():
            post.save()
            print(post)
            return redirect("AddProfile")

    else:
         post=forms.PostForm()
    return render(request,'add_post.html',{'form':post})