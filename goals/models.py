from django.db import models
from django.conf import settings
from django.urls import reverse

class Goal(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='goals'
    )
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    target = models.PositiveIntegerField(help_text="Target value (e.g., steps, calories)")
    achieved = models.PositiveIntegerField(default=0, help_text="Achieved value")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def get_absolute_url(self): 
        return reverse('goals:goal_detail', kwargs={'pk': self.pk})