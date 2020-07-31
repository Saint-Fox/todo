from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Task
from .forms import TaskForm, UpdateTaskForm


def main_view(request):
    tasks = Task.objects.all()
    form = TaskForm()
    
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {
        'tasks': tasks,
        'form': form,
    }
    return render(request, 'tasks/main.html', context)

def update_task(request, pk):
    task = Task.objects.get(id=pk)
    update_form = UpdateTaskForm(instance=task)
    
    if request.method == "POST":
        update_form = UpdateTaskForm(request.POST, instance=task)
        if update_form.is_valid():
            update_form.save()
            return redirect('/')
    
    context = {
        'task': task,
        'update_form': update_form,
    }
    return render(request, 'tasks/update_task.html', context)

def delete_task(request, pk):
    task = Task.objects.get(id=pk)
    
    if request.method == "POST":
        task.delete()
        return redirect('/')
    
    context = {
        'task': task,
    }
    return render(request, 'tasks/delete.html', context)