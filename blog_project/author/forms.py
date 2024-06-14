from django import forms 
from . import models
# from .models import Author

class AuthorForm(forms.ModelForm):
    class Meta:
        model=models.Author
        fields='__all__' # sob attibute gula use korsi
        # exclude=['bio'] # bio attibute bad diye sob use kormu