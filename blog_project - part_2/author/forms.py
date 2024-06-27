from django import forms 
from . import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
# from .models import Author
# class AuthorForm(forms.ModelForm):
#     class Meta:
#         model=models.Author
#         fields='__all__' # sob attibute gula use korsi
        # exclude=['bio'] # bio attibute bad diye sob use kormu


class RegistrationFrom(UserCreationForm):
    first_name=forms.CharField(widget=forms.TextInput(attrs={'id':'required'}))
    last_name=forms.CharField(widget=forms.TextInput(attrs={'id':'required'}))

    class Meta:
        model=User
        fields=['username','first_name','last_name','email']
        


class ChangeUserForm(UserChangeForm):
    password=None
    class Meta:
        model=User
        fields=['username',"first_name",'last_name','email']