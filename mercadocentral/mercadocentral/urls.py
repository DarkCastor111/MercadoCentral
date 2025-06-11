"""
URL configuration for mercadocentral project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from core import views
from usuarios.urls import usuarios_patterns
from footer.urls import footer_patterns
from django.conf import settings

urlpatterns = [
#    path('', views.home, name="core_home"),
    path('', views.AnunciosListView.as_view(), name='core_home'),
    path('<int:pk>/<slug:page_slug>/', views.AnuncioDetailView.as_view(), name='core_anuncio'),
    path('misanuncios/', views.MisAnunciosListView.as_view(), name='core_mis'),
    path('favoritos/', views.AnunciosFavoritosListView.as_view(), name='core_fav'),
    path('nv_anuncio/', views.AnuncioCreateView.as_view(), name='core_nv_anun' ),
    path('up_anuncio/<int:pk>/<slug:page_slug>/', views.AnuncioUpdateView.as_view(), name='core_up_anun' ),
    path('reservar/', views.api_reservar, name='api_reservar' ),
    path('desactivar/<int:pk_an>/', views.api_desactivar, name='api_desactivar' ),
    path('admin/', admin.site.urls),
    # Paths de Auth
    path('usuarios/', include(usuarios_patterns)),
    # path('usuarios/', include('django.contrib.auth.urls')),
    # Path de footer
    path('footer/', include(footer_patterns)),
    # Temporal

]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
