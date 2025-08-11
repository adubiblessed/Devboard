from django.shortcuts import render,redirect

from .forms import UserForm, LoginForm
from .models import User
from taskmanage.models import Task
from notes.models import Note

# Create your views here.

def home (request): 
    tasks = Task.objects.all()
    notes = Note.objects.all()
    print(notes)
    total_tasks = tasks.count()
    completed_tasks = tasks.filter(completed=True).count()

    if total_tasks == 0:
        percent_complete = 0
    else:
        percent_complete = int((completed_tasks / total_tasks) * 100)
    return render(request, 'base/main.html',{'tasks': tasks, 'percent_complete': percent_complete, 'notes':notes})



def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('login')
    else:
        form = UserForm()
    return render(request, 'base/register.html', {'form': form})   


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = User.objects.get(username=username)
            if user.check_password(password):
                request.session['user_id'] = user.id
                return redirect('home')
            else:
                form.add_error(None, "Invalid username or password.")
    else:
        form = LoginForm()
    return render(request, 'base/login.html', {'form': form})