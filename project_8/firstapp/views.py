from django.shortcuts import render,redirect
from . import forms
# from .forms import userChanges
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
# Create your views here.

def Home(request):
    return render(request,'home.html')


def SignUp_pages(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            data=forms.RegisterForm(request.POST)
            if data.is_valid():
                messages.success(request,'Account created successfully')
                data.save()
                print(data.cleaned_data)
        else:
            data=forms.RegisterForm()      
        return render(request,'signup.html',{'form':data})
    else:
        return redirect('profile')


def Login(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            form=AuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                name=form.cleaned_data['username']
                userpass=form.cleaned_data['password']
                user=authenticate(username=name,password=userpass) # check korlam data ache kina 

                if user is not None:
                    login(request,user)
                    return redirect('profile')

        else:
            form=AuthenticationForm()
        return render(request,'login.html',{'form':form})
    else:
        return redirect('profile')


def Profile(request):
    if  request.user.is_authenticated:
        if request.method=='POST':
            data=forms.userChanges(request.POST,instance=request.user)
            if data.is_valid():
                messages.success(request,'Account updated successfully')
                data.save()
                print(data.cleaned_data)
        else:
            data=forms.userChanges(instance=request.user)      
        return render(request,'profile.html',{'form':data})
    else:
        return redirect('signup')


def LogOut(request):
    logout(request)
    return redirect('login')


def passWord_changes(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            form=PasswordChangeForm(user=request.user,data=request.POST)
            if form.is_valid():
                user=form.save()
                update_session_auth_hash(request,user)
                return redirect('profile')        
        else:
            form=PasswordChangeForm(user=request.user)
        return render(request,'passChanges.html',{'form':form})
    else:
        return redirect('login')
    

def passWord_changes2(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            form=SetPasswordForm(user=request.user,data=request.POST)
            if form.is_valid():
                user=form.save()
                update_session_auth_hash(request,user)
                return redirect('profile')        
        else:
            form=SetPasswordForm(user=request.user)
        return render(request,'passChanges.html',{'form':form})
    else:
        return redirect('login')
    



def Changes_User_Data(request):
    if  request.user.is_authenticated:
        if request.method=='POST':
            data=forms.ChangeUserData(request.POST,instance=request.user)
            if data.is_valid():
                messages.success(request,'Account updated successfully')
                data.save()
                print(data.cleaned_data)
        else:
            data=forms.ChangeUserData()      
        return render(request,'profile.html',{'form':data})
    else:
        return redirect('signup')