from django.shortcuts import render, redirect
from . import forms
from . import models
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def add_post(request):
    if request.method=='POST':
        post=forms.PostForm(request.POST)
        if post.is_valid():
            post.instance.author=request.user
            post.save()
            print(post)
            return redirect("add_post")

    else:
         post=forms.PostForm()
    return render(request,'add_post.html',{'form':post})

@login_required
def edit_post(request,id):
     post=models.Post.objects.get(pk=id)
     post_form=forms.PostForm(instance=post)
     if request.method=='POST':
        post_form=forms.PostForm(request.POST,instance=post)
        if post_form.is_valid():
            post_form.instance.author=request.user
            post_form.save()
            print(post_form)
            return redirect("homepages")

     return render(request,'add_post.html',{'form':post_form})



@login_required
def delete_post(request,id):
    del_post=models.Post.objects.get(pk=id)
    del_post.delete()
    return redirect("homepages")
