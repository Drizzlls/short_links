# from django import forms
# from .models import Agent,Manager
#
# class CreateLink(forms.ModelForm):
#
#     class Meta:
#             model = Agent
#             fields = ['name','surname','link_agent','agent_phone','manager_personal']
#             widgets = {
#                 'name' : forms.TextInput(attrs={"class":"form-control"}),
#                 'surname' : forms.TextInput(attrs={"class":"form-control"}),
#                 'agent_phone': forms.TextInput(attrs={"class": "form-control","type":"tel","placeholder": '+7 (999) 999-99-99'}),
#                 'link_agent': forms.TextInput(attrs={"class": "form-control", 'readonly' : 'readonly',"id":"linkForAgent"}),
#                 'manager_personal': forms.Select(attrs={"class": "form-select", 'readonly' : 'readonly',"id":"inputSelectCountry"}),
#             }
#
#
