from ast import BoolOp
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render, get_object_or_404
from django.views import generic

from .serializers import TaskSerializer
from .models import Task
# Create your views here.
def index(request):
    context = {

    }
    return render(request, 'index.html', context)

@api_view(['GET','POST'])
def task(request):
    if request.method == 'GET':
        task = Task.objects.all()
        serializer = TaskSerializer(task, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE', 'GET'])
def taskDetail(request, pk):
    try:
        task = get_object_or_404(Task, pk=pk)
    except Task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'DELETE':
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'GET':
        if task.status == True:
            task.status = False
        else:
            task.status = True
        task.save()
        return Response(status=status.HTTP_202_ACCEPTED)