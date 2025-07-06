from django.urls import path
from .views import TaskListView, TaskUpdateDeleteView

urlpatterns = [
    path('todo/', TaskListView.as_view(), name='task-list'),
    path('todo/<int:pk>/', TaskUpdateDeleteView.as_view(), name='task-detail'),
]
