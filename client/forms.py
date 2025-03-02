# client/forms.py
from django import forms

class MixxClientForm(forms.Form):
    amount = forms.DecimalField(
        label="Montant",
        decimal_places=0,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Entrez le montant'})
    )
    personal_code = forms.CharField(
        label="Code personnel",
        max_length=20,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Entrez votre code personnel'})
    )

class MoovClientForm(forms.Form):
    secret_code = forms.CharField(
        label="Code secret",
        max_length=20,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Entrez votre code secret'})
    )