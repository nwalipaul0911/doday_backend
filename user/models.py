from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
  gender_choices = (
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'Other'),
  )

  email= models.CharField(max_length=50 ,unique=True)
  username = models.CharField(max_length=50 ,unique=True)
  first_name = models.CharField(max_length=50)
  last_name = models.CharField(max_length=50)
  gender = models.CharField(max_length=50 ,choices=gender_choices)
  country = models.CharField(max_length=50)
  state = models.CharField(max_length=50)

  REQUIRED_FIELDS = ['username', 'first_name', 'last_name']
  USERNAME_FIELD = 'email'

  def __str__(self) -> str:
    return self.username