from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import status
from user.models import User
from .models import Note
from .serializers import NoteSerializer


# Create your views here.
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def notes(request):
  user = request.user
  if request.method == 'GET':
    notes = Note.objects.all().filter(owner=user)
    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
  elif request.method == 'POST':
    data = JSONParser().parse(request)
    serializer = NoteSerializer(data=data)
    if serializer.is_valid():
      serializer.save(owner=request.user)
      return Response(status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def note(request, id):
  user = request.user
  note = get_object_or_404(Note, id=id)
  if request.method == 'GET':
    serializer = NoteSerializer(note)
    return Response(serializer.data, status=status.HTTP_200_OK)
  elif request.method == 'PUT':
    data = JSONParser().parse(request)
    serializer = NoteSerializer(note, data=data)
    if serializer.is_valid():
      serializer.save()
      return Response(status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)
  elif request.method == 'DELETE':
    note.delete()
    return Response(status=status.HTTP_200_OK)