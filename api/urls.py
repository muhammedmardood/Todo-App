from django.urls import path
from .views import *

urlpatterns = [
    path('task-list/', taskList),
]
