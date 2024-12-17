from django import forms
from .models import Workout

class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ['name', 'duration', 'calories_burned', 'description']
        
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g., Morning Run'
            }),
            'duration': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g., 30',
                'min': '1'
            }),
            'calories_burned': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g., 250',
                'min': '0'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Optional notes, e.g., felt strong today.'
            }),
        }
        
        labels = {
            'name': 'Workout Name',
            'duration': 'Duration (minutes)',
            'calories_burned': 'Calories Burned (optional)',
            'description': 'Notes (optional)',
        }
        
        help_texts = {
            'duration': 'Enter the workout length in minutes.',
            'calories_burned': 'Approximate calories burned, if known.'
        }
