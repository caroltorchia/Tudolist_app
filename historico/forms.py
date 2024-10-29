# forms.py
from django import forms
from .models import Nota

class NotaForm(forms.ModelForm):
    class Meta:
        model = Nota
        fields = ['disciplina', 'tipo', 'nota']
        widgets = {
            'disciplina': forms.Select(attrs={'class': 'form-select form-control'}),
            'tipo': forms.Select(attrs={'class': 'form-select form-control'}),
            'nota': forms.NumberInput(attrs={'class': 'form-control'})
        }
