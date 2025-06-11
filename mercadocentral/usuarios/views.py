from django.shortcuts import render
from django.views.generic import CreateView
from django.views.generic.edit import UpdateView
from django.contrib.auth.models import User

from django.urls import reverse_lazy
from .forms import UsuarioCreationForm, PersoChangeFormCustom

# Create your views here.
class AltaView(CreateView):
    form_class = UsuarioCreationForm
    template_name = 'usuarios/signup.html'

    def get_success_url(self):
        return reverse_lazy('usu_login') + '?register'
    
class UserChangeView(UpdateView):
    model = User
    form_class = PersoChangeFormCustom
    success_url = reverse_lazy('usu_perso')
    template_name = 'usuarios/perso_form.html'

    def get_success_url(self):
        return reverse_lazy('usu_perso') + '?changed'
    
    def get_object(self, queryset=None): # type: ignore
        user = self.request.user
        if not user.is_authenticated:
            from django.core.exceptions import PermissionDenied
            raise PermissionDenied("User must be authenticated")
        return user




