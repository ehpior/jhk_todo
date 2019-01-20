from django.shortcuts import get_object_or_404, render
from todo.models import Ttodo
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from datetime import datetime
import time


def index(request):
    todo_list = Ttodo.objects.all()
    todo_fin = []
    todo_ing = []
    todo_over = []
    todo_notfin = []
    for obj in todo_list:
        if obj.complete == True:
            todo_fin.append(obj)
        else:
            todo_notfin.append(obj)
            if not obj.deadline:
                todo_ing.append(obj)
            elif obj.deadline < datetime.date(datetime.now()):
                todo_over.append(obj)
            else:
                todo_ing.append(obj)
    return render(request, 'todo/index.html', {'todo_fin': todo_fin,'todo_ing': todo_ing, 'todo_over': todo_over, 'todo_notfin': todo_notfin, 'todo_list': todo_list})


def detail(request,todo_id):
    todo = get_object_or_404(Ttodo, pk=todo_id)
    return render(request, 'todo/detail.html', {'todo': todo})


def create(request):
    if request.method == "POST":
        k = request.POST
        if not k['deadline']:
            new_Ttodo = Ttodo.objects.create(title=k['title'],content=k['content'])
        else:
            new_Ttodo = Ttodo.objects.create(title=k['title'],content=k['content'],deadline=k['deadline'])
        return HttpResponseRedirect(reverse('todo:index'))
    return render(request, 'todo/create.html')


def modify(request,todo_id):
    todo = get_object_or_404(Ttodo, pk=todo_id)
    todo_deadline = str(todo.deadline)
    if request.method == "POST":
        k = request.POST
        if k['deadline']=='':
            Ttodo.objects.filter(pk=todo_id).update(title=k['title'],content=k['content'])
        else:
            Ttodo.objects.filter(pk=todo_id).update(title=k['title'],content=k['content'],deadline=k['deadline'])
        return HttpResponseRedirect(reverse('todo:detail',kwargs={'todo_id': todo_id}))
    return render(request, 'todo/modify.html', {'todo': todo,'todo_deadline': todo_deadline})


def delete(request,todo_id):
    todo = get_object_or_404(Ttodo, pk=todo_id)
    todo.delete()
    return HttpResponseRedirect(reverse('todo:index'))

