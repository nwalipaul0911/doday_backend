from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ['id', 'email', 'username', 'first_name', 'last_name','gender','country','state']
    
  def create(self, data):
    if data['password1']==data['password2']:
      user = User.objects.create(
        username=data['username'],
        email=data['email'],
        first_name=data['first_name'],
        last_name=data['last_name'],
        country=data['country'],
        state=data['state'],
        gender=data['gender'],
      )
      user.set_password(data['password1'])
      user.save()
      return user


