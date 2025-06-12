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
        return reverse_lazy('login') + '?register'
    
    def form_valid(self, form):
        new_email = form.cleaned_data.get('email')
        if User.objects.filter(email=new_email).exists():
            form.add_error('email', 'Ya existe un usuario con este email.')
            return self.form_invalid(form)
        return super().form_valid(form)
    
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
    
    def form_valid(self, form):
        new_email = form.cleaned_data.get('email')
        if User.objects.filter(email=new_email).exists():
            form.add_error('email', 'Ya existe un usuario con este email.')
            return self.form_invalid(form)
        return super().form_valid(form)




