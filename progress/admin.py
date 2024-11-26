from django.contrib import admin
from .models import Progress

@admin.register(Progress)
class ProgressAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'weight', 'body_fat_percentage', 'muscle_mass', 'created_at', 'updated_at')
    search_fields = ('user__username', 'notes')
    list_filter = ('user', 'date', 'created_at', 'updated_at')