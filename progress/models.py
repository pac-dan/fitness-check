from django.db import models
from django.conf import settings
from django.urls import reverse

class Progress(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='progress_entries'
    )
    date = models.DateField()
    weight = models.FloatField(help_text="Weight in kilograms")
    body_fat_percentage = models.FloatField(help_text="Body fat percentage")
    muscle_mass = models.FloatField(help_text="Muscle mass in kilograms", blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-date', '-created_at']
    
    def __str__(self):
        return f"Progress on {self.date}"
    
    def get_absolute_url(self):
        return reverse('progress:progress_detail', kwargs={'pk': self.pk})
