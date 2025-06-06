from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.utils.text import slugify
from .models import Anuncio, Mensaje
from .forms import AnuncioForm

# Create your views here.


def home(request):
    return render(request, "core/layout.html")

class AnunciosListView(ListView):
    model = Anuncio

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['origen'] = "global"
        return context


    def get_queryset(self):

        queryset = super().get_queryset()
        get_gen = self.request.GET.get('genero')
        get_pre = self.request.GET.get('prenda')

        if get_gen:
            filtro_gen = get_gen
            self.request.session['genero'] = get_gen
        else:
            filtro_gen = self.request.session.get('genero', "GEN_ALL")

        if get_pre:
            filtro_pre = get_pre
            self.request.session['prenda'] = get_pre
        else:
            filtro_pre = self.request.session.get('prenda', "PRD_ALL")

        if (filtro_gen != "GEN_ALL"):
            if (filtro_gen == "GEN_MX"):
                valores = [filtro_gen, "GEN_NO", "GEN_NA"]
            else:
                valores = [filtro_gen, "GEN_MX"]
            queryset = queryset.filter(genero__in=valores)

        if (filtro_pre != "PRD_ALL"):
            if (filtro_pre == "PRD_UN"):
                valores=["PRD_UN_PAN", "PRD_UN_SUE", "PRD_UN_FAL", "PRD_UN_POL", "PRD_NIN"]
            elif (filtro_pre == "PRD_DP"):
                valores=["PRD_DP_PAN", "PRD_DP_BER", "PRD_DP_POL", "PRD_DP_CHQ", "PRD_DP_CHD", "PRD_NIN"]
            else:
                valores=[filtro_pre, "PRD_NIN"]
            queryset = queryset.filter(prenda__in=valores)

        return queryset


class AnuncioDetailView(DetailView):
    model = Anuncio

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        anuncio = self.get_object()
        # Get distinct authors of mensajes for this anuncio
        context['interesados_usernames'] = list(set(
            Mensaje.objects.filter(anuncio=anuncio)
            .values_list('author__username', flat=True)
        ))
        context['origen']=self.request.GET.get('origen')
        return context
    
@method_decorator(login_required, name='dispatch')   
class MisAnunciosListView(ListView):
    model= Anuncio

    def get_queryset(self):

        queryset = super().get_queryset()
        queryset = queryset.filter(usuario = self.request.user)
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['origen'] = "mis"
        return context


@method_decorator(login_required, name='dispatch')       
class AnunciosFavoritosListView(ListView):
    model = Anuncio

    def get_queryset(self):
        queryset = super().get_queryset()
        user = self.request.user
        queryset = queryset.filter(mensajes_anuncio__author=user).distinct()
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['origen'] = "favs"
        return context


@method_decorator(login_required, name='dispatch')    
class AnuncioCreateView(CreateView):
    model = Anuncio
    form_class = AnuncioForm

    # redirección
    success_url = reverse_lazy('core_mis')

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)
    
def api_reservar(request):
    pk_anuncio = request.POST["form_pk_anuncio"]
    ancio = Anuncio.objects.get(pk=pk_anuncio)
    msj = request.POST["form_mensaje"]


    if not msj or msj.strip() == "":
        messages.warning(request, "El mensaje no puede estar vacío.")
        return redirect('core_anuncio', pk=pk_anuncio, page_slug=slugify(ancio.designacion))

    try:
        com = Mensaje.objects.create(
            anuncio=ancio,
            author=request.user,
            texto=msj
        )
        com.save()
    except (IntegrityError, ValueError):
        messages.warning(request, "Error al guardar el mensaje.")
        return redirect('core_anuncio', pk=pk_anuncio, page_slug=slugify(ancio.designacion))

    messages.success(request, "Mensaje guardado correctamente.")
    return redirect('core_anuncio', pk=pk_anuncio, page_slug=slugify(ancio.designacion))



