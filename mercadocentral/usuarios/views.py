from django.shortcuts import render
from django.views.generic import CreateView
from .forms import UsuarioCreationForm

# Create your views here.
class AltaView(CreateView):
    form_class = UsuarioCreationForm
    template_name = 'usuarios/signup.html'
