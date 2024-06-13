from django import forms
from . import models

class StudentForm(forms.ModelForm):
    class Meta:
        model=models.StudentModal
        fields='__all__'
        labels={
            'name':'Student Name',
            'roll':'Student Roll'
        }
        widgets={
            'roll': forms.PasswordInput()
        }