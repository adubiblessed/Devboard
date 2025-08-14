from django.shortcuts import render,redirect
from django.utils import timezone

from .forms import UserForm, LoginForm
from .models import User
from taskmanage.models import Task
from notes.models import Note
from django.contrib.auth.decorators import login_required
from streak.models import Streak
from django.contrib.auth import authenticate, login as auth_login

# Create your views here.

def home (request):
    if not request.user.is_authenticated:
        return redirect('login')
    # create streak if it doesn't exist
    if not hasattr(request.user, 'streak'):
        Streak.objects.create(
        user=request.user,
        start_date=timezone.now().date(),
        last_activity=timezone.now().date(),
        streak_count=0
    )
    user = request.user
    request.user.streak.update_streak()
    streak_count = request.user.streak.streak_count 
    tasks = Task.objects.filter(user=user).order_by('-created_at')
    notes = Note.objects.order_by('-created_at')[:3]
    total_tasks = tasks.count()
    completed_tasks = tasks.filter(completed=True).count()

    if total_tasks == 0:
        percent_complete = 0
    else:
        percent_complete = int((completed_tasks / total_tasks) * 100)
    return render(request, 'base/main.html',{
                                             'tasks': tasks, 
                                             'percent_complete': percent_complete, 
                                             'notes':notes, 
                                             'streak_count': streak_count
                                             })



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
            user=authenticate(request,username=username, password=password)
            
            if user is not None:
                auth_login(request, user)
                return redirect('home')
            else:
                form.add_error(None, "Invalid username or password.")
            
            return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'base/login.html', {'form': form})