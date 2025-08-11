from django.views.generic.detail import DetailView

from django.shortcuts import render, redirect
from django.utils.text import slugify
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from core.models import Anuncio
from .models import Hilo, Post


# Create your views here.
@method_decorator(login_required, name="dispatch")
class HiloDetailView(DetailView):
    model = Hilo

    '''
    def get_object(self):
        hilo = super(HiloDetailView, self).get_object()
        if self.request.user not in hilo.users.all():
            raise Http404()
        return hilo
    '''



def api_reservar(request):
    pk_anuncio = request.POST["form_pk_anuncio"]
    ancio = Anuncio.objects.get(pk=pk_anuncio)
    msj = request.POST["form_mensaje"]


    if not msj or msj.strip() == "":
        messages.warning(request, "El mensaje no puede estar vacío.")
        return redirect('core_anuncio', pk=pk_anuncio, page_slug=slugify(ancio.designacion))
    
    # Encontrar el hilo
    hilo = Hilo.objects.encontrar_o_crear(ancio, request.user) # type: ignore

    try:
        ancio.mensajes += 1
        ancio.save()
        
        '''
        com = Mensaje.objects.create(
            anuncio=ancio,
            author=request.user,
            texto=msj
        )
        '''
        pst = Post.objects.create(
            author = request.user,
            contenido = msj
        )

        pst.save()

        hilo.posts.add(pst)
        hilo.save()

    except (IntegrityError, ValueError):
        messages.warning(request, "Error al guardar el mensaje.")
        return redirect('core_anuncio', pk=pk_anuncio, page_slug=slugify(ancio.designacion))

    messages.success(request, "Mensaje guardado correctamente.")
    return redirect('core_anuncio', pk=pk_anuncio, page_slug=slugify(ancio.designacion))
