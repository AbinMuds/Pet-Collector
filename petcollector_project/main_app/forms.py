from django import forms
from .models import Feeding,Pet

class FeedingForm(forms.ModelForm):
    class Meta:
        model = Feeding
        fields = ['date', 'meal']

class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields= ['name', 'species', 'breed', 'description', 'age']
