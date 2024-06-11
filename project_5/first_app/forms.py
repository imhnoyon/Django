
from typing import Any
from django import forms
from django.core import validators

class contactForm(forms.Form):
    name=forms.CharField(label="UserName", widget=forms.TextInput(attrs={'placeholder':'Enter your Name'}))
    # file=forms.FileField()
    email=forms.EmailField(label="UserEmail")
    age=forms.IntegerField(label="Ages")
    weight=forms.FloatField(label="Weight", required=False)
    balance=forms.DecimalField(required=False)
    Birthday=forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    Appointment=forms.CharField(widget=forms.DateInput(attrs={'type':'datetime-local'}))
    check=forms.BooleanField()
    CHOICES=[('S','Small'),('M','Medium'),('L','Large')]
    size=forms.ChoiceField(choices=CHOICES)



class studentForm(forms.Form):
    name=forms.CharField(label="Name",widget=forms.TextInput(attrs={'placeholder':'Enter Your Name:'}),validators=[validators.MinLengthValidator(10,message='at least 10 character')])
    email=forms.EmailField()
    file=forms.FileField(validators=[validators.FileExtensionValidator(allowed_extensions=['pdf','png'])])

    # def clean_name(self):
    #     valname=self.cleaned_data['name']
        
    #     if len(valname) < 10:
    #         raise forms.ValidationError("Enter a name at least 10 characters")
    #     return valname
    
    # def clean_email(self):
    #     emailvalue=self.cleaned_data['email']
    #     if '.com' not in emailvalue:
    #         raise forms.ValidationError("Your email must be '.com' added")
    #     return emailvalue


    # def clean(self):
    #     cleaned_data= super().clean()
    #     valname=self.cleaned_data['name']
    #     valemail=self.cleaned_data['email']

    #     if len(valname) < 10:
    #         raise forms.ValidationError("Your name must be 10 character")
    #     if '.com' not in valemail:
    #         raise forms.ValidationError('Your email must be added .com ')



class passwordValidation(forms.Form):
    name=forms.CharField(widget=forms.TextInput)
    password=forms.CharField(widget=forms.PasswordInput)
    re_password=forms.CharField(widget=forms.PasswordInput)
    

    def clean(self):
        # cleaned_data=self.super().clean()
        val_name=self.cleaned_data['name']
        val_pass=self.cleaned_data['password']
        val_rePass=self.cleaned_data['re_password']

        if len(val_name) < 10:
            raise forms.ValidationError("Your name must be 10 character")
        if val_pass != val_rePass:
            raise forms.ValidationError("Password doesn't match")
        










