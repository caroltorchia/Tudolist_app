# forms.py
from django import forms
from .models import Nota


class NotaForm(forms.ModelForm):
    class Meta:
        model = Nota
        fields = ["disciplina", "tipo", "nota", "observacoes"]
        widgets = {
            "disciplina": forms.Select(attrs={"class": "form-select form-control"}),
            "tipo": forms.Select(attrs={"class": "form-select form-control"}),
            "nota": forms.NumberInput(attrs={"class": "form-control"}),
            "observacoes": forms.Textarea(attrs={"class": "form-control"}),
        }
