from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from .models import Todo


def index(request):
    todo = Todo.objects.all()
    return render(request, 'todoapp/index.html',
                  {'todo_list': todo, 'title': 'Главная страница'})


@require_http_methods(['POST'])
@csrf_exempt
def add(request):
    title = request.POST['title']
    todo = Todo(title=title)
    todo.save()
    return redirect('index')


def update(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.is_complete = not todo.is_complete
    todo.save()
    return redirect('index')


def delete(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.delete()
    return redirect('index')