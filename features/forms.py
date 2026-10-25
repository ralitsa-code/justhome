from django import forms
from .models import Feature

class FeatureForm(forms.ModelForm):
    class Meta:
        model = Feature
        fields = ['name']

        labels = {
            'name': "Feature name",
        }

        help_texts = {
            'name': "Enter a unique feature name up to 30 characters.",
        }