from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from . import forms
from . import models

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView,UpdateView,DeleteView,DetailView
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


# using class based views
@method_decorator(login_required,name='dispatch')
class AddClassBasedView(CreateView):
    model=models.Post
    form_class =forms.PostForm
    template_name = 'add_post.html'
    success_url = reverse_lazy('add_post')
    def form_valid(self, form):
        form.instance.author=self.request.user
        return super().form_valid(form)




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



# update or edit class based views
@method_decorator(login_required,name='dispatch')
class EditPost(UpdateView):
    model=models.Post
    form_class=forms.PostForm
    template_name='add_post.html'
    pk_url_kwarg='id'
    success_url=reverse_lazy('profile')




@login_required
def delete_post(request,id):
    del_post=models.Post.objects.get(pk=id)
    del_post.delete()
    return redirect("homepages")



# delete class based views
@method_decorator(login_required,name='dispatch')
class DeletePost(DeleteView):
    model=models.Post
    template_name='delete.html'
    pk_url_kwarg='id'
    success_url=reverse_lazy('profile')



class DetailsPost(DetailView):
    model=models.Post
    pk_url_kwarg='id'
    template_name='details_post.html'


    def post(self,request,*args,**kwargs):
        comment_form=forms.CommentForm(data=self.request.POST)
        post=self.get_object()
        if comment_form.is_valid():
            new_comment=comment_form.save(commit=False)
            new_comment.post=post
            new_comment.save()
        return self.get(request,*args,**kwargs)
         
            
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        post=self.object
        comments=post.comments.all()
        comment_form=forms.CommentForm()
        context['comments']=comments
        context['comment_form']=comment_form
        return context

