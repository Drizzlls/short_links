from django import forms
from .models import Agent
from managers.models import Manager
from links.views import generageLink


class AddAgent(forms.ModelForm):

    class Meta:
        model = Agent
        fields = ['name', 'surname', 'agent_phone', 'manager_personal', 'link_agent']
        widgets = {
            'name': forms.TextInput(attrs={"class": "form-control"}),
            'surname': forms.TextInput(attrs={"class": "form-control"}),
            'agent_phone': forms.TextInput(attrs={"class": "form-control","type":"tel","placeholder": '+7 (999) 999-99-99'}),
            'manager_personal': forms.Select(attrs={"class": "form-select", 'readonly' : 'readonly',"id":"inputSelectCountry"}),
            'link_agent': forms.TextInput(attrs={"class": "form-control", 'readonly' : 'readonly',"id":"linkForAgent", "value": generageLink()}),
        }