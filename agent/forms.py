# agent/forms.py
from django import forms

class MixxAgentForm(forms.Form):
    agent_number = forms.CharField(
        label="Numéro d'agent",
        max_length=20,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Entrez votre numéro d\'agent'})
    )

class MoovAgentForm(forms.Form):
   agent_number = forms.CharField(
        label="Numéro d'agent",
        max_length=20,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Entrez votre numéro d\'agent'})
    )