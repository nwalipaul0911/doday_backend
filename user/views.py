from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import status
from .models import User
from .serializers import UserSerializer



from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        # ...
        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
# Create your views here.
@api_view(['POST'])
def register_view(request):
  data = JSONParser().parse(request) 
  serializer = UserSerializer(data=data)
  if serializer.is_valid():
    serializer.create(data=data)
    return Response(status=status.HTTP_201_CREATED)
  return Response(status=status.HTTP_400_BAD_REQUEST) 

@api_view(['GET'])
def profile_view(request, id):
  user = get_object_or_404(User, id=id)
  serializer = UserSerializer(user)
  return Response(serializer.data, status=status.HTTP_200_OK)




    
    