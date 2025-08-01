from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User

class UsuarioCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

class PersoChangeFormCustom(UserChangeForm):
    class Meta:
        model = User
        fields = ("username", "email")


