"""Forms of the project."""
from django import forms
from django.core.validators import MaxLengthValidator
from .models import Thing
# Create your forms here.

class ThingForm(forms.ModelForm):
    class Meta:
        model = Thing
        fields = ['name', 'description', 'quantity']

    description = forms.CharField(
        widget=forms.Textarea(),
        max_length=120
        )
    quantity = forms.NumberInput()