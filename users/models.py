from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MinValueValidator


class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)
    height = models.FloatField(
        null=True, 
        blank=True,
        validators=[MinValueValidator(0.0, message="Height must be a positive number")]
    )
    weight = models.FloatField(
        null=True, 
        blank=True,
        validators=[MinValueValidator(0.0, message="Weight must be a positive number")]
    )

    def __str__(self):
        return self.username