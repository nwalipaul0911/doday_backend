from django.db import models
from user.models import User

# Create your models here.
class Note(models.Model):
  title = models.CharField(max_length=50)
  detail = models.TextField(max_length=255)
  owner = models.ForeignKey(User, on_delete=models.CASCADE)
  
  def __str__(self) -> str:
    return self.title