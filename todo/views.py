from django.shortcuts import get_object_or_404, render
from todo.models import Ttodo
from django.contrib.auth.models import User
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
    todo_content = get_object_or_404(Ttodo, key=todo_id)
    return render(request, 'todo/detail.html', {'todo_content': todo_content})

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
    todo_content = get_object_or_404(Ttodo, key=todo_id)
    
    return render(request, 'todo/modify.html', {'todo_content': todo_content})

def delete(request,todo_id):
    todo_content = get_object_or_404(Ttodo, key=todo_id)
    
    return render(request, 'todo/delete.html', {'todo_content': todo_content})

