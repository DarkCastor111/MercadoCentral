from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.mixins import UserPassesTestMixin
from django.utils.decorators import method_decorator
from django.utils.text import slugify
from .models import Anuncio, Mensaje
from .forms import AnuncioForm

# Create your views here.


def home(request):
    return render(request, "core/layout.html")

class AnunciosListView(ListView):
    model = Anuncio
    paginate_by = 8

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['origen'] = "global"
        return context


    def get_queryset(self):

        queryset = super().get_queryset().filter(activo=True)
        get_tal = self.request.GET.get('talla')
        get_pre = self.request.GET.get('prenda')

        if get_pre:
            filtro_pre = get_pre
            self.request.session['prenda'] = get_pre
        else:
            filtro_pre = self.request.session.get('prenda', "PRD_ALL")

        if get_tal:
            filtro_tal = get_tal
            self.request.session['talla'] = get_tal
        else:
            filtro_tal = self.request.session.get('talla', "TAL_ALL")


        if (filtro_tal != "TAL_ALL"):
            queryset = queryset.filter(talla=filtro_tal)
            # queryset = queryset.filter(talla__in=valores)


        if (filtro_pre != "PRD_ALL"):
            queryset = queryset.filter(prenda=filtro_pre)


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
        queryset = super().get_queryset().filter(activo=True)
        queryset = queryset.filter(usuario = self.request.user).order_by('-updated')
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['origen'] = "mis"
        return context


@method_decorator(login_required, name='dispatch')       
class AnunciosFavoritosListView(ListView):
    model = Anuncio

    def get_queryset(self):
        queryset = super().get_queryset().filter(activo=True)
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
    


@method_decorator(login_required, name='dispatch')    
class AnuncioUpdateView( UserPassesTestMixin, UpdateView):
    model = Anuncio
    form_class = AnuncioForm
    template_name = 'core/anuncio_form.html'
    success_url = reverse_lazy('core_mis')

    def test_func(self):
        anuncio = self.get_object()
        return self.request.user == anuncio.usuario or self.request.user.is_superuser # type: ignore

    
def api_reservar(request):
    pk_anuncio = request.POST["form_pk_anuncio"]
    ancio = Anuncio.objects.get(pk=pk_anuncio)
    msj = request.POST["form_mensaje"]


    if not msj or msj.strip() == "":
        messages.warning(request, "El mensaje no puede estar vacío.")
        return redirect('core_anuncio', pk=pk_anuncio, page_slug=slugify(ancio.designacion))

    try:
        ancio.mensajes += 1
        ancio.save()
        
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

def api_desactivar(request, pk_an):
    if not pk_an:
        messages.error(request, "No se ha especificado el anuncio a desactivar.")
        return redirect('core_mis')

    try:
        anuncio = Anuncio.objects.get(pk=pk_an)
        if request.user == anuncio.usuario or request.user.is_superuser:
            anuncio.activo = False
            anuncio.save()
            messages.success(request, "El anuncio ha sido desactivado correctamente.")
        else:
            messages.error(request, "No tienes permiso para desactivar este anuncio.")
    except Anuncio.DoesNotExist:
        messages.error(request, "El anuncio no existe.")

    return redirect('core_mis')

