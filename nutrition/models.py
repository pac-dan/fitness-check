from django.db import models
from django.conf import settings
from django.urls import reverse

class Nutrition(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='nutrition_entries'
    )
    meal_type = models.CharField(max_length=100, choices=[
        ('breakfast', 'Breakfast'),
        ('lunch', 'Lunch'),
        ('dinner', 'Dinner'),
        ('snack', 'Snack'),
        ('other', 'Other'),
    ])
    food_items = models.TextField(help_text="List of food items consumed")
    calories = models.PositiveIntegerField(help_text="Total calories consumed")
    protein = models.FloatField(help_text="Protein intake in grams")
    carbs = models.FloatField(help_text="Carbohydrate intake in grams")
    fats = models.FloatField(help_text="Fat intake in grams")
    date = models.DateField(auto_now_add=True)
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-date', '-created_at']
    
    def __str__(self):
        return f"{self.meal_type.capitalize()} on {self.date}"
    
    def get_absolute_url(self):
        return reverse('nutrition:nutrition_detail', kwargs={'pk': self.pk})
