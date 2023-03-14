from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from user.models import User
from .models import Todo, ExecutionRequest
from .serializers import TodoSerializer, ExecutionRequestSerializer
from django.db.models import Q

# Create your views here.
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def todos(request):
  user = request.user
  if request.method == 'GET':
    todos = Todo.objects.all().filter(Q(owner=user) | Q(executors__username=user)).order_by("-todo_date")
    serializer = TodoSerializer(todos, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
  elif request.method == 'POST':
    data = JSONParser().parse(request)
    serializer = TodoSerializer(data=data)
    if serializer.is_valid():
      serializer.save(owner=request.user)
      return Response(serializer.data, status=status.HTTP_201_CREATED)
  return Response({'message':'active'})

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def todo(request, id):
  user = request.user
  todo = get_object_or_404(Todo, id=id)
  if request.method == 'GET':
    serializer = TodoSerializer(todo)
    return Response(serializer.data, status=status.HTTP_200_OK)
  elif request.method == 'PUT':
    data = JSONParser().parse(request)
    serializer = TodoSerializer(todo, data=data)
    if serializer.is_valid():
      serializer.save()
      return Response(status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)
  elif request.method == 'DELETE':
    todo.delete()
    return Response(status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def execution_request(request, task_id):
  data = JSONParser().parse(request)
  sender = request.user
  email = data['email']
  receiver = get_object_or_404(User, Q(email=email)|Q(username=email))
  task = get_object_or_404(Todo, id=task_id)
  if receiver is not None:
    execution = ExecutionRequest.objects.create(sender = sender, receiver = receiver, task = task)
    execution.save()
    return Response(status=status.HTTP_200_OK)
  return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def setTodoStatus(request, id):
  task = get_object_or_404(Todo, id=id)
  task.setStatus()
  return Response(status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def accept_request(request, request_id):
  exe_request = get_object_or_404(ExecutionRequest, id=request_id)
  exe_request.accept(user = request.user)
  return Response(status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def decline_request(request, request_id):
  exe_request = get_object_or_404(ExecutionRequest, id=request_id)
  exe_request.decline(user = request.user)
  return Response(status=status.HTTP_200_OK)
