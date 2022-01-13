from django.urls import path
from .views import *

urlpatterns = [
    path('task-list/', taskList),
    path('task/<int:pk>/', taskDetails),
    path('task/delete/<int:pk>/', taskDelete)
]
