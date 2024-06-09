
from django import forms

class contactForm(forms.Form):
    name=forms.CharField(label="UserName")
    file=forms.FileField()
    # email=forms.EmailField(label="UserEmail")
    # age=forms.IntegerField(label="Ages")
    # weight=forms.FloatField(label="Weight")
    # balance=forms.DecimalField()
    # Birthday=forms.DateField()
    # check=forms.BooleanField()
    # CHOICES=[('S','Small'),('M','Medium'),('L','Large')]
    # size=forms.ChoiceField(choices=CHOICES)
