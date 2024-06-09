from django.urls import path,include
from . import views
urlpatterns = [
    
    path('',views.form,name='forms'),
    path('about/',views.about,name='about'),
    path('django_form/',views.django_form,name='django_Form'),
]