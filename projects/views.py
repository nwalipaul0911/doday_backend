from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from user.models import User
from .models import Project
from .serializers import ProjectSerializer
from todo.serializers import TodoSerializer, Todo
from django.db.models import Q
from user.serializers import UserSerializer
from rest_framework import status


# Create your views here.
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def projects_view(request):
  user = request.user
  if request.method == 'GET':
    projects = Project.objects.filter(Q(owner=user) | Q(collaborators__username=user.username))
    serializer = ProjectSerializer(projects, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
  elif request.method == 'POST':
    data = JSONParser().parse(request)
    serializer = ProjectSerializer(data=data)
    if serializer.is_valid():
      serializer.save(owner=user)
      return Response(status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def project_view(request, id):
  project = get_object_or_404(Project, id=id)
  if request.method == 'GET':
    serializer = ProjectSerializer(project)
    return Response(serializer.data, status=status.HTTP_200_OK)
  elif request.method == 'PUT':
    data = JSONParser().parse(request)
    serializer = ProjectSerializer(project, data=data)
    if serializer.is_valid():
      serializer.save()
      return Response(status=status.HTTP_200_OK)
  elif request.method =='DELETE':
    project.delete()
    return Response(status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def addExistingTask(request, task_id, project_id):
  task = get_object_or_404(Todo, id=task_id)
  project = get_object_or_404(Project, id=project_id)
  project.add_task(task)
  return Response(status = status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addNewTask(request, project_id):
  project = get_object_or_404(Project, id=project_id)
  data = JSONParser().parse(request)
  serializer = TodoSerializer(data=data)
  if serializer.is_valid():
    serializer.save(owner=request.user)
  task = get_object_or_404(Todo, title=data['title'])
  project.add_task(task)
  return Response(status = status.HTTP_201_CREATED)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def removeTask(request, task_id, project_id):
  project = get_object_or_404(Project, id=project_id)
  task = get_object_or_404(Todo, id=task_id)
  project.remove_task(task)
  return Response(status = status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def project_tasks(request, id):
  project = get_object_or_404(Project, id=id)
  tasks = project.tasks.all()
  serializer = TodoSerializer(tasks, many=True)
  return Response(serializer.data, status= status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addCollaborator(request, project_id):
  data =JSONParser().parse(request)
  email = data['email']
  user = request.user
  if user['email'] != email:
    project = get_object_or_404(Project, id=project_id)
    collaborator = get_object_or_404(User, email=email)
    if collaborator is not None:
      project.add_collaborator(collaborator)
      return Response( status=status.HTTP_201_CREATED)
  return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def removeCollaborator(request, project_id, collaborator_id):
  project = get_object_or_404(Project, id=project_id)
  collaborator = get_object_or_404(User, id=collaborator_id)
  project.remove_collaborator(collaborator)
  return Response(status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def project_collaborators(request, id):
  project = get_object_or_404(Project, id=id)
  collaborators = project.collaborators.all()
  serializer = UserSerializer(collaborators, many=True)
  return Response(serializer.data, status=status.HTTP_200_OK)

