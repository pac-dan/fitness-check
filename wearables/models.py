from django.db import models
from django.conf import settings
from django.urls import reverse 

class Wearable(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='wearables'
    )
    device_name = models.CharField(max_length=255)
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    purchase_date = models.DateField()
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)   

class Meta: 
    ordering = ['-purchase_date', '-created_at']

def __str__(self):
    return f"{self.device_name} ({self.brand} {self.model})"
    
def get_absolute_url(self):
    return reverse('wearables:wearable_detail', kwargs={'pk': self.pk})