from django import forms
from .models import Manager


class AddManager(forms.ModelForm):

    class Meta:
        model = Manager
        fields = ['name', 'surname','idFromBitrix']
        widgets = {
            'name': forms.TextInput(attrs={"class": "form-control"}),
            'surname': forms.TextInput(attrs={"class": "form-control"}),
            'idFromBitrix': forms.TextInput(attrs={"class": "form-control"}),
        }