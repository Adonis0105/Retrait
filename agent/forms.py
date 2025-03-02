# agent/forms.py
from django import forms

class MixxAgentForm(forms.Form):
    agent_number = forms.CharField(
        label="Numéro d'agent",
        max_length=20,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Entrez votre numéro d\'agent'})
    )

class MoovAgentForm(forms.Form):
    client_number = forms.CharField(
        label="Numéro du client",
        max_length=20,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Entrez le numéro du client'})
    )
    amount = forms.DecimalField(
        label="Montant",
        decimal_places=0,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Entrez le montant'})
    )
    agent_number = forms.CharField(
        label="Numéro d'agent",
        max_length=20,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Entrez votre numéro d\'agent'})
    )