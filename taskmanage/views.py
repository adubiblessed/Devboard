from django.shortcuts import render, redirect, get_object_or_404
from .forms import TaskForm
from .models import Task

def task_display(request):
    tasks = Task.objects.all()
    return render(request, 'base/task_display.html', {'tasks': tasks})

def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tasks_display')  
    else:
        form = TaskForm()
    return render(request, 'base/task_create.html', {'form': form})

def toggle_complete(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.completed = not task.completed
    task.save()
    return redirect('tasks_display')  
