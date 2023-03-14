from django.db import models
from user.models import User

# Create your models here.
class Todo(models.Model):
  title = models.CharField(max_length=50)
  detail = models.TextField(max_length=255)
  todo_date = models.DateField()
  todo_time = models.TimeField()
  status = models.BooleanField(default=False)
  owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='todo')
  executors = models.ManyToManyField(User, blank=True, related_name='executors')
  done_by = models.ForeignKey(User,blank=True, on_delete=models.SET_NULL, null=True, related_name='done_by')

  def setStatus(self):
    if self.status is False:
      self.status = True
      self.save()
    else: 
      self.status = False
      self.save()
  
  def __str__(self) -> str:
    return self.title

  def addExecutor(self, user):
    if user not in self.executors.all():
      self.executors.add(user)

  def removeExecutor(self, user):
    if user in self.executors.all():
      self.executors.add(user)

class ExecutionRequest(models.Model):
  sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
  receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver')
  active = True
  timestamp = models.TimeField(auto_now_add=True)
  task = models.ForeignKey(Todo, on_delete=models.CASCADE)

  def accept(self, user):
    self.task.addExecutor(user)


  def decline(self, user):
    self.active = False