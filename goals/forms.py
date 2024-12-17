from django import forms
from .models import Goal

class GoalForm(forms.ModelForm):
    class Meta:
        model = Goal
        fields = ['title', 'target', 'description']
        
        labels = {
            'title': 'Goal Title',
            'target': 'Target',
            'description': 'Description (optional)',
        }
        
        help_texts = {
            'target': 'Enter a numeric target (e.g., steps, distance, weight, or workout count).',
        }
        
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g., Run 5km without stopping'
            }),
            'target': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': '1',
                'placeholder': 'e.g., 5000 steps per day'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Add details or motivation for your goal.'
            }),
        }
