from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')        # Show these columns in the list
    search_fields = ('name', 'email')       # Enable search bar
    list_filter = ('name',) 