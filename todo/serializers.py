from rest_framework.serializers import ModelSerializer
from .models import Todo, ExecutionRequest

class TodoSerializer(ModelSerializer):
  class Meta:
    model = Todo
    fields = ['id','title', 'detail', 'todo_date', 'todo_time', 'status']

class ExecutionRequestSerializer(ModelSerializer):
  class Meta:
    model = ExecutionRequest
    fields = ['task']