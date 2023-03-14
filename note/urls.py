from django.urls import path
from .views import *
urlpatterns = [
  path('', notes),
  path('<int:id>', note),

]