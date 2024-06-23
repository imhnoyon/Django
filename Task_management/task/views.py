# from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import TaskModel
from .forms import TaskForm
from category.models import TaskCategory
from . import models
# Create your views here.


def add_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_tasks')
    else:
        form = TaskForm()
    return render(request, 'add_task.html', {'form': form})

def show_tasks(request):
    tasks = TaskModel.objects.all()
    return render(request, 'show_tasks.html', {'tasks': tasks})

def edit_task(request, pk):
    task = models.TaskModel.objects.get(pk=pk)
    form=TaskForm(instance=task)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('show_tasks')
    else:
        form = TaskForm(instance=task)
    return render(request, 'edit_task.html', {'form': form})

def delete_task(request, pk):
    task = models.TaskModel.objects.get(pk=pk)
    task.delete()
    return redirect('show_tasks')


