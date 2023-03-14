from django.db import models

# Create your models here.

from django.db import models
from user.models import User

# Create your models here.
class Team(models.Model):
  name = models.CharField(max_length=50)
  creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='creator')
  admin = models.ManyToManyField(User, blank=True)
  members = models.ManyToManyField(User, blank=True),

  def __str__(self):
    return self.name

  def add_member(self, user):
    if not user in self.members.all():
      self.members.add(user)
    else: pass

  def remove_member(self, user):
    if user in self.members.all():
      self.members.remove(user)
    else: pass

  def add_admin(self, user):
    if not user in self.admin.all():
      self.admin.add(user)
    else: pass

  def remove_admin(self, user):
    if user in self.admin.all():
      self.admin.remove(user)
    else: pass

class MembershipRequest(models.Model):
  sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='membership_sender')
  receiver = models.ForeignKey(User, on_delete=models.CASCADE,related_name='membership_receiver')
  timestamp = models.DateField(auto_now_add=True)
  is_active = models.BooleanField(blank=True, null=False, default=True)
  team = models.ForeignKey(Team, null=False, on_delete=models.CASCADE)

  def __str__(self) -> str:
    return self.sender

  def accept(self):
    self.team.add_member(self.receiver)
  
  def decline(self):
    self.is_active = False
    self.delete()


