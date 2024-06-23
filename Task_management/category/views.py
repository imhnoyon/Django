from django.shortcuts import render, redirect
from .models import TaskCategory
from .forms import CategoryForm
# Create your views here.



def add_category(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_category')
    else:
        form = CategoryForm()
    return render(request, 'category/add_category.html', {'form': form})
