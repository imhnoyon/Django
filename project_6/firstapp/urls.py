from django.urls import path
from . import views
urlpatterns = [
   
    path('',views.home, name='homepages'),
    path('delete/<int:roll>',views.delete_student, name='delete_students'),
    path('home2/',views.home2,name='home2'),
]
