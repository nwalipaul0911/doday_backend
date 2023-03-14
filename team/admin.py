from django.contrib import admin
from .models import Team, MembershipRequest

# Register your models here.
@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
  list_display = ['name', 'creator']
  list_display_links = ['name']
  list_filter = ['name']
  search_fields = ['name']

@admin.register(MembershipRequest)
class MembershipRequestAdmin(admin.ModelAdmin):
  list_display = ['team', 'sender', 'receiver']
  list_display_links = ['team']
  list_filter = ['team']
  search_fields = ['team']
