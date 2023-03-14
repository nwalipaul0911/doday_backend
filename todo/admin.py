from django.contrib import admin
from .models import Todo, ExecutionRequest
# Register your models here.
@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
  list_display = ('id', 'title')
  list_display_links = ('title',)
  list_filter = ('title',)
  search_fields = ('title',)

@admin.register(ExecutionRequest)
class ExecutionRequestAdmin(admin.ModelAdmin):
  list_display = ('id', 'task')
  list_display_links = ('id',)