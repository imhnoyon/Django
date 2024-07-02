from django import forms 
from . import models

class PostForm(forms.ModelForm):
    class Meta:
        model=models.Post
        # fields='__all__'
        exclude=['author']


class CommentForm(forms.ModelForm):
    class Meta:
        model=models.Comment
        fields=['name','email','body']
        
        