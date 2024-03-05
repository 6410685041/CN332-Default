from django import forms
from .models import Intersection

class IntersectionForm(forms.ModelForm):
    class Meta:
        model = Intersection
        fields = ['intersection_name', 'location']