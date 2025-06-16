from django import forms

class CorreoContactoForm(forms.Form):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class':'form-control'}), min_length=3, max_length=100)
    mensaje = forms.CharField(required=True, widget=forms.Textarea(attrs={'class':'form-control', 'rows':4, 'placeholder':'Su mensaje'}), min_length=10, max_length=1000)
    tema = forms.CharField(required=False, widget=forms.HiddenInput)

    def clean_tema(self):
        data = self.cleaned_data['tema']
        if data:
            raise forms.ValidationError("Bot detectado.")
        return data