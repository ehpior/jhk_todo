from django.urls import path
from . import views

app_name = 'todo'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('complete/', views.complete, name='complete'),
    path('<int:todo_id>/', views.detail, name='detail'),
    path('<int:todo_id>/modify/', views.modify, name='modify'),
    path('<int:todo_id>/delete/', views.delete, name='delete'),
    path('<int:todo_id>/complete/', views.make_complete, name='make_complete')
]