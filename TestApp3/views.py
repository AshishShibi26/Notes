from django.shortcuts import render, redirect
from .models import Note

def index(request):
    tasks = Note.objects.all()
    if request.method == 'POST':
        a = request.POST.get('title')
        b = request.POST.get('content')
        Note.objects.create(title=a, content=b)
    return render(request, 'index.html',{'tasks':tasks})

def delete(request, id):

    note = Note.objects.get(id=id)

    note.delete()

    return redirect('/')