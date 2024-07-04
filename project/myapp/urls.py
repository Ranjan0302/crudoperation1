from django.urls import path
from .views import user,tasks

urlpatterns = [
    path('user/',user,name='user'),
    path('tasks/',tasks,name='tasks'),
]