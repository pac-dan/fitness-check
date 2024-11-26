from django.contrib import admin
from .models import Notification

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'read', 'created_at', 'updated_at')
    search_fields = ('title', 'message', 'user__username')
    list_filter = ('user', 'read', 'created_at', 'updated_at')
