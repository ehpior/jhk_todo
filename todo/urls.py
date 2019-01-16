from django.urls import path
from . import views

app_name = 'todo'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:todo_id>/', views.detail, name='detail'),
    path('create/', views.create, name='create'),
    path('modify/', views.modify, name='modify'),
    path('delete/', views.delete, name='delete'),
]