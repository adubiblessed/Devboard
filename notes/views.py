from django.shortcuts import render, redirect

from .models import Note
from .forms import NoteForm

# Create your views here.
def notes_display(request):
    notes =  Note.objects.order_by('-created_at')
    
    return render(request, 'base/notes_display.html', { 'notes':notes })

def note_create(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('notes_display')  
    else:
        form = NoteForm()
    return render(request, 'base/note_create.html', {'form': form})

def note_each(request, note_id):
    note = Note.objects.get(id=note_id)
    return render(request, 'base/note_each.html', {'note': note})