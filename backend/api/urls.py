from django.urls import path
from . import views

urlpatterns = [
    path('todo', views.TodoItemListCreate.as_view(), name='todo-list-create'),
    path('todo/<int:pk>', views.TodoItemRetrieveUpdateDestroy.as_view(), name='todo-retrieve-update-destroy'),
]
