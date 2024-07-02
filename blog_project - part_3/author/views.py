from django.shortcuts import render,redirect
from . import forms
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from posts.models import Post
from django.contrib.auth.views import LoginView,LogoutView
from django.urls import reverse_lazy
# Create your views here.

# def add_author(request):
#     if request.method=='POST':
#         author_form=forms.AuthorForm(request.POST)
#         if author_form.is_valid():
#             author_form.save()
#             print(author_form)
#             return redirect('add_author')
        
#     else:
#         author_form=forms.AuthorForm()
#     return render(request,'add_author.html',{'form': author_form})



def register(request):
    if request.method=='POST':
        register_form=forms.RegistrationFrom(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request,'Register Successfully')
            print(register_form)
            return redirect('register')
        
    else:
        register_form=forms.RegistrationFrom()
    return render(request,'register.html',{'form': register_form,'type':'Register'})



def user_login(request):
    if request.method=='POST':
        form=AuthenticationForm(request,request.POST)
        if form.is_valid():
            messages.success(request,'Loggin Successfully')
            user_name=form.cleaned_data['username']
            user_pass=form.cleaned_data['password']
            user=authenticate(username=user_name,password=user_pass)
            if user is not None:
                login(request,user)
                return redirect('profile')
        else:
            messages.warning(request,'Login information is incorrect')
            print('else login')
            return redirect('login')
            
    else:
        form=AuthenticationForm()
    return render(request,'register.html',{'form':form,'type':'Login'})



# login views to change class based views

class users_login(LoginView):
    template_name='register.html'
    def get_success_url(self):
        return reverse_lazy('profile')
    
    def form_valid(self, form):
        messages.success(self.request,'Loggin in Successfully')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.success(self.request,'Loggin Information is Incorrect')
        return super().form_invalid(form)
    
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs) 
        context["type"] = 'Login'
        return context
        
        
    

@login_required
def profile(request):
    data=Post.objects.filter(author=request.user)
    return render(request,'profile.html',{'form':data})

@login_required
def Edit_profile(request):
    if request.method=='POST':
        profile_form=forms.ChangeUserForm(request.POST,instance=request.user)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request,'Profile updated Successfully')
            print(profile_form)
            return redirect('profile')
        
    else:
        profile_form=forms.ChangeUserForm(instance=request.user)
    return render(request,'update_profile.html',{'form': profile_form,'type':'Edit Profile'})


def Logout(request):
    logout(request)
    return redirect('login')


#logout class based views

class user_logout(LogoutView):
    success_url=reverse_lazy('homepages')






def pass_change(request):
    if request.method=='POST':
       form=PasswordChangeForm(request.user,data=request.POST)
       if form.is_valid():
            update_session_auth_hash(request,form.user)
            form.save()
            messages.success(request,'Password Change Successfully')
            print(form)
            return redirect('profile')
        
    else:
        form=PasswordChangeForm(user=request.user)
    return render(request,'pass_change.html',{'form': form,'type':'Password change'})
