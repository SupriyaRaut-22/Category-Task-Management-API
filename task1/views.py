from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Task1
from .serializers import TaskSerializer
from rest_framework.response import Response
from django.http import JsonResponse

def api_home(request):
    return JsonResponse({"message": "Welcome to Task Management API"})

@api_view(['POST'])
def create_task(request):
    """create new task"""
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_task(request):
    """fetch all tasks"""
    tasks= Task1.objects.all()
    serializer = TaskSerializer(tasks,many = True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_one_task(request,id):
    
    try:
        task=Task1.objects.get(pk=id)
    except Task1.DoesNotExist:
        return Response({"Error:Task not Found"}, status=status.HTTP_404_NOT_FOUND)
    
    """get one single task"""

    serializer=TaskSerializer(task)
    return Response(serializer.data)
    
@api_view(['PUT'])
def update_task(request,id):
    
    try:
        task=Task1.objects.get(pk=id)
    except Task1.DoesNotExist:
        return Response({"Error:Task not Found"}, status=status.HTTP_404_NOT_FOUND) 
    
    """Update a task"""
 
    serializer=TaskSerializer(task, data=request.data,partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_task(request,id):
    """Delete a task"""
    try:
        task=Task1.objects.get(pk=id)
    except:
        return Response({"Error:Task not Found"},status=status.HTTP_404_NOT_FOUND)
    
    task.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)