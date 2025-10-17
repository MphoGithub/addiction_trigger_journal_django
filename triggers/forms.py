from django import forms
from .models import Trigger

class TriggerForm(forms.ModelForm):
    
    class Meta:
        model = Trigger 
        fields = ["name","description","category","coping_strategy"]

