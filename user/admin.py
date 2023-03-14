from django.contrib import admin
from .models import User

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
  list_display = ('id', 'username' )
  list_display_links = ('username',)
  list_filter = ('username',)
  search_fields = ('username',)