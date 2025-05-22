from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Anuncio

# Create your views here.


def home(request):
    return render(request, "core/layout.html")

class AnunciosListView(ListView):
    model = Anuncio

class AnuncioDetailView(DetailView):
    model = Anuncio