from django import forms
from .models import Items

class ItemsUpdateForm(forms.ModelForm):
    class Meta:
        model = Items
        fields = ['name', 'description', 'price', 'quantity', 'date_updated']

class AddItemForm(forms.ModelForm):
    class Meta:
        model = Items
        fields = ['name', 'description', 'price', 'quantity', 'date_updated']
