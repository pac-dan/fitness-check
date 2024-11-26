from django.contrib import admin
from .models import Nutrition

@admin.register(Nutrition)
class NutritionAdmin(admin.ModelAdmin):
    list_display = ('meal_type', 'user', 'calories', 'protein', 'carbs', 'fats', 'created_at', 'updated_at')
    search_fields = ('meal_type', 'food_items', 'user__username')
    list_filter = ('user', 'created_at', 'updated_at')
