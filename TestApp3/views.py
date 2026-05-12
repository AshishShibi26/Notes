from django.shortcuts import render, redirect
from .models import Note


# HOME PAGE + ADD NOTE

def index(request):

    notes = Note.objects.all()

    if request.method == 'POST':

        title = request.POST.get('title')

        content = request.POST.get('content')

        Note.objects.create(
            title=title,
            content=content
        )

        return redirect('/')

    return render(request, 'index.html', {
        'notes': notes
    })


# DELETE NOTE

def delete(request, id):

    note = Note.objects.get(id=id)

    note.delete()

    return redirect('/')


# UPDATE NOTE

def update(request, id):

    note = Note.objects.get(id=id)

    notes = Note.objects.all()

    if request.method == 'POST':

        note.title = request.POST.get('title')

        note.content = request.POST.get('content')

        note.save()

        return redirect('/')

    return render(request, 'index.html', {
        'note': note,
        'notes': notes
    })