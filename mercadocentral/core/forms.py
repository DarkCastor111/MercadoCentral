from django import forms
import bleach
from .models import Anuncio

class AnuncioForm(forms.ModelForm):

    class Meta:
        model = Anuncio
        fields = ['foto', 'designacion', 'descripcion', 'prenda', 'talla', 'estado', 'materia'] # 'genero',
        widgets = {
            'designacion': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Titulo'}),
            'foto' : forms.ClearableFileInput(attrs={'class':'form-control-file mt-3'}),
            'descripcion': forms.Textarea(attrs={'class':'form-control'}),
            'prenda': forms.Select(attrs={'class': 'form-select'}),
            'talla': forms.Select(attrs={'class': 'form-select'}),
            # 'genero': forms.Select(attrs={'class': 'form-select'}),
            'estado': forms.Select(attrs={'class': 'form-select'}),
            'materia': forms.Select(attrs={'class': 'form-select'}),
        }
        labels = {
            'designacion': '',
            'descripcion': '',
        }
    
    def clean_descripcion(self):
        descripcion = self.cleaned_data.get('descripcion', '')
        # Allow only safe tags, or none
        allowed_tags = []  # or ['b', 'i', 'br', ...] if you want to allow some
        return bleach.clean(descripcion, tags=allowed_tags, strip=True)
