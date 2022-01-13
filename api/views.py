from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *

current_url = "http://127.0.0.1:8000/api/"


@api_view(['GET'])
def main(request):
    api_urls = {
        'List and Create Tasks': current_url+'task-list/',
        'Get Details and Update a Task': current_url+'task/TASK_ID/',
        'Delete a Task': current_url+'task/delete/TASK_ID/',
    }

    return Response(api_urls)


@api_view(["GET", "POST"])
def taskList(request):
    if request.method == "GET":
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def taskDetails(request, pk):
    task = Task.objects.get(id=pk)
    if request.method == "GET":
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = TaskSerializer(instance=task, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)


@api_view(['DELETE'])
def taskDelete(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return Response("item was deleted successfully")
