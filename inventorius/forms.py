from django import forms
from .models import Inventorius

class InventoriusForm(forms.ModelForm):
    class Meta:
        model = Inventorius
        fields = '__all__'
