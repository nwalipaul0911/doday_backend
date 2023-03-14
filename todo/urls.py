from django.urls import path
from .views import *
urlpatterns = [

  path('', todos),
  path('<int:id>', todo),
  path('execution_request/<int:task_id>', execution_request),
  path('set_status/<int:id>', setTodoStatus),
  path('accept_request/<int:task_id>', accept_request),
  path('decline_request/<int:task_id>', decline_request),
]