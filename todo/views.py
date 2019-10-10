from django.shortcuts import render, redirect
from django.utils import timezone
from .models import todo

# Create your views here.


def home(request):
    todo_items = todo.objects.filter(active=1).order_by('-created')
    to_homepage = {
        'todo_items': todo_items,
    }
    return render(request, 'todo/home.html', to_homepage)


def add_todo(request):
    created = timezone.now()
    text = request.POST['text']
    todo.objects.create(created=created, text=text)
    return redirect('home')


def delete_todo(request, todo_id):
    t = todo.objects.get(id=todo_id)
    t.active = 0
    t.save()
    return redirect('home')
