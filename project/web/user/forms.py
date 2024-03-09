from django import forms
from .models import Profile

class OccupationForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['occupation']
        labels = {
            'occupation': 'Select Occupation',
        }
