from django import forms
from .models import Nutrition


class NutritionForm(forms.ModelForm):
    class Meta:
        model = Nutrition
        fields = ['meal_type', 'food_items', 'calories', 'protein', 
                 'carbs', 'fats', 'notes']

        labels = {
            'meal_type': 'Meal Type',
            'food_items': 'Food Items',
            'calories': 'Calories (optional)',
            'protein': 'Protein (g, optional)',
            'carbs': 'Carbs (g, optional)',
            'fats': 'Fats (g, optional)',
            'notes': 'Notes (optional)',
        }

        help_texts = {
            'food_items': '',
            'calories': 'Total estimated calories for this meal, if known.',
        }

        widgets = {
            'meal_type': forms.Select(attrs={
                'class': 'form-control'
            }),
            'food_items': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'e.g., Oatmeal, banana, coffee'
            }),
            'calories': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': '0',
                'placeholder': 'e.g., 500'
            }),
            'protein': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': 'any',
                'min': '0',
                'placeholder': 'e.g., 20'
            }),
            'carbs': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': 'any',
                'min': '0',
                'placeholder': 'e.g., 40'
            }),
            'fats': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': 'any',
                'min': '0',
                'placeholder': 'e.g., 15'
            }),
            'notes': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Additional details like mood or hunger level.'
            }),
        }
