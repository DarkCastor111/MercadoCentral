from django import forms
from .models import Anuncio

class AnuncioForm(forms.ModelForm):

    class Meta:
        model = Anuncio
        fields = ['foto', 'designacion', 'descripcion', 'genero', 'estado', 'prenda', 'talla']
        widgets = {
            'designacion': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Titulo'}),
            'foto' : forms.ClearableFileInput(attrs={'class':'form-control-file mt-3'}),
            'descripcion': forms.Textarea(attrs={'class':'form-control'}),
            'talla': forms.NumberInput(attrs={'class':'form-control'}),
            'genero': forms.Select(attrs={'class': 'form-select'}),
            'estado': forms.Select(attrs={'class': 'form-select'}),
            'prenda': forms.Select(attrs={'class': 'form-select'}),
        }
        labels = {
            'designacion': '',
            'descripcion': '',
        }
