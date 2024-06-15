from django.shortcuts import render
from posts import models
def home(request):
    data=models.Post.objects.all()
    print(data)
    return render(request,'home.html',{'form':data})