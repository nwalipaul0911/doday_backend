from django.db import models
from user.models import User
from todo.models import Todo

# Create your models here.


class Project(models.Model):
  name = models.CharField(max_length=50)
  owner = models.ForeignKey(User,null=True, on_delete=models.CASCADE, related_name='owner')
  tasks = models.ManyToManyField(Todo, blank=True, related_name='task')
  collaborators = models.ManyToManyField(User, blank=True, related_name='collaborators')

  def __str__(self):
    return self.name

  def add_task(self, task):
      self.tasks.add(task)

  def remove_task(self, task):
    if task in self.tasks.all():
      self.tasks.remove(task)
    else:
      pass

  def add_collaborator(self, user):
    if user not in self.collaborators.all():
      self.collaborators.add(user)

  def remove_collaborator(self, user):
    if user in self.collaborators.all():
      self.collaborators.remove(user)






