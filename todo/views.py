from django.shortcuts import get_object_or_404, render
from todo.models import Ttodo
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

def index(request):
    todo_list = Ttodo.objects.all()
    todo_fin = []
    todo_not = []
    for obj in todo_list:
        if obj.complete == True:
            todo_fin.append(obj)
        else:
            todo_not.append(obj)
    return render(request, 'todo/index.html', {'todo_fin': todo_fin,'todo_not': todo_not})

def detail(request,todo_id):
    todo = get_object_or_404(Ttodo, pk=todo_id)
    return render(request, 'todo/detail.html', {'todo': todo})

def create(request):
    if request.method == "POST":
        k = request.POST
        if k['deadline']=='':
            new_Ttodo = Ttodo.objects.create(title=k['title'],content=k['content'])
        else:
            new_Ttodo = Ttodo.objects.create(title=k['title'],content=k['content'],deadline=k['deadline'])
        return HttpResponseRedirect(reverse('todo:index'))
    return render(request, 'todo/create.html')

def modify(request,todo_id):
    todo = get_object_or_404(Ttodo, pk=todo_id)
    if request.method == "POST":
        k = request.POST
        if k['deadline']=='':
            Ttodo.objects.filter(pk=todo_id).update(title=k['title'],content=k['content'])
        else:
            Ttodo.objects.filter(pk=todo_id).update(title=k['title'],content=k['content'],deadline=k['deadline'])
        return HttpResponseRedirect(reverse('todo:detail',kwargs={'todo_id': todo_id}))
    return render(request, 'todo/modify.html', {'todo': todo})

def delete(request,todo_id):
    todo = get_object_or_404(Ttodo, pk=todo_id)
    todo.delete()
    return HttpResponseRedirect(reverse('todo:index'))

