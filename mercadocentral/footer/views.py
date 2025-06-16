from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from .forms import CorreoContactoForm

# Create your views here.
def footer_detail_view(request):
    if request.method == "POST":
        form_recibido = CorreoContactoForm(request.POST)
        if form_recibido.is_valid():
            email = form_recibido.cleaned_data['email']
            mensaje = form_recibido.cleaned_data['mensaje']
            author = request.user.username if request.user.is_authenticated else "No registrado"
            try:
                send_mail(
                    subject=f"{author} : Contacto desde MercadoCentral",
                    message=f"De: {author} ({email})\n\nMensaje:\n\n{mensaje}",
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=['dragosoftcanarias@gmail.com'],
                )
                messages.success(request, "¡Tu mensaje ha sido enviado correctamente!")
            except Exception as e :
                txt_msg = 'Ocurrió un error al enviar el mensaje.'
                if settings.DEBUG:
                    txt_msg += f'{type(e).__name__} -> {str(e)}'
                messages.warning(request, txt_msg)
        else:
            messages.warning(request, "Ocurrió un error al validar el formulario.")
        return redirect(reverse_lazy('footer_detail') + "#contacto")

    else:
        init_datos = {}
        if request.user.is_authenticated:
            init_datos['email'] = request.user.email
        form_recibido = CorreoContactoForm(initial = init_datos)
    
    return render(request, "footer/footer-detail.html", {'form_contacto': form_recibido}) # reverse_lazy('footer_detail') , {'form_contacto': form_recibido})

