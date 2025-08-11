from django.urls import path
from .views import HiloDetailView, api_reservar

mensajero_patterns = ([
    # path('', HiloListView.as_view(), name='hlist'),
    path('hilo/<int:pk>/', HiloDetailView.as_view(), name='hdetail'),
    path('reservar/', api_reservar, name='api_reservar'),
    # path('hilo/<int:p_pk>/anadir', anadir_mensaje, name='hadd'),
    # path('hilo/start/<p_username>', iniciar_hilo, name='hiniciar'),
], 'mensajero')