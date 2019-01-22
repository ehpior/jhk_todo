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


def complete(request):
    todo_fin = Ttodo.objects.filter(complete=True)

    return render(request, 'todo/complete.html', {'todo_fin': todo_fin})

def make_complete(request,todo_id):
    todo = get_object_or_404(Ttodo, pk=todo_id)
    if todo.complete:
        Ttodo.objects.filter(pk=todo_id).update(complete=False)
        return HttpResponseRedirect(reverse('todo:complete'))
    else:
        Ttodo.objects.filter(pk=todo_id).update(complete=True)
        return HttpResponseRedirect(reverse('todo:index'))


def detail(request,todo_id):
    todo = get_object_or_404(Ttodo, pk=todo_id)

    return render(request, 'todo/detail.html', {'todo': todo})


def create(request):
    if request.method == "POST":
        k = request.POST
        if k['deadline']:
            new_Ttodo = Ttodo.objects.create(title=k['title'],content=k['content'],deadline=k['deadline'],priority=k.get('priority'))
        elif not k['deadline']:
            new_Ttodo = Ttodo.objects.create(title=k['title'],content=k['content'],priority=k.get('priority'))

        return HttpResponseRedirect(reverse('todo:index'))
    return render(request, 'todo/create.html')


def modify(request,todo_id):
    todo = get_object_or_404(Ttodo, pk=todo_id)
    if request.method == "POST":
        k = request.POST
        if k['deadline'] and k.get('priority'):
            Ttodo.objects.filter(pk=todo_id).update(title=k['title'],content=k['content'],deadline=k['deadline'],priority=k.get('priority'))
        elif not k['deadline'] and not k.get('priority'):
            Ttodo.objects.filter(pk=todo_id).update(title=k['title'],content=k['content'])
        elif not k.get('priority'):
            Ttodo.objects.filter(pk=todo_id).update(title=k['title'],content=k['content'],deadline=k['deadline'])
        elif not k['deadline']:
            Ttodo.objects.filter(pk=todo_id).update(title=k['title'],content=k['content'],priority=k.get('priority'))
        return HttpResponseRedirect(reverse('todo:index'))
    return render(request, 'todo/modify.html', {'todo': todo})


def delete(request,todo_id):
    todo = get_object_or_404(Ttodo, pk=todo_id)
    todo.delete()
    return HttpResponseRedirect(reverse('todo:index'))

