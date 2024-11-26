from django.contrib import admin
from .models import Goal

@admin.register(Goal)
class GoalAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'target', 'achieved', 'created_at', 'updated_at')
    search_fields = ('title', 'description', 'user__username')
    list_filter = ('user', 'created_at', 'updated_at')
