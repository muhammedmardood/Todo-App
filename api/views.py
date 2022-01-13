from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import * 

@api_view(["GET", "POST"])
def taskList(request):
    task = Task.objects.all()
    serializer = TaskSerializer(task, many=True)

    return Response(serializer.data)
