from django.urls import path
from .views import *

urlpatterns = [
  path('', projects_view),
  path('<int:id>', project_view),
  path('tasks/<int:id>', project_tasks),
  path('collaborators/<int:id>', project_collaborators),
  path('add_task/<int:task_id>/<int:project_id>', addExistingTask),
  path('add_new_task/<int:project_id>', addNewTask),
  path('remove_task/<int:task_id>/<int:project_id>', removeTask),
  path('add_collaborator/<int:project_id>', addCollaborator),
  path('remove_collaborator/<int:collaborator_id>/<int:project_id>', removeCollaborator),
]