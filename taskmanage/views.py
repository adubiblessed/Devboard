from django.shortcuts import render, redirect

from .forms import TaskForm
from .models import Task

# Create your views here.
def task_display(request):
    tasks = Task.objects.all()
     
    return render(request, 'base/task_display.html', {
        'tasks': tasks
    } )

def task_create(request):
    form = TaskForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('task_display')
    else:
        form = TaskForm()

    context = {'form':form}
    return render(request, 'base/task_create.html', context)