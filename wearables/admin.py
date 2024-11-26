from django.contrib import admin
from .models import Wearable

@admin.register(Wearable)
class WearableAdmin(admin.ModelAdmin):
    list_display = ('device_name', 'brand', 'model', 'user', 'purchase_date', 'created_at', 'updated_at')
    search_fields = ('device_name', 'brand', 'model', 'user__username')
    list_filter = ('brand', 'purchase_date', 'created_at', 'updated_at')
