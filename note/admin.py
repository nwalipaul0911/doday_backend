from django.contrib import admin
from .models import Note
# Register your models here.
@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
  list_display = ('id', 'title')
  list_display_links = ('title',)
  list_filter = ('title',)
  search_fields = ('title',)