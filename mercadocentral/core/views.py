from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Anuncio

# Create your views here.


def home(request):
    return render(request, "core/layout.html")

class AnunciosListView(ListView):
    model = Anuncio

    def get_queryset(self):

        queryset = super().get_queryset()
        get_gen = self.request.GET.get('genero')
        get_pre = self.request.GET.get('prenda')

        if get_gen:
            filtro_gen = get_gen
            self.request.session['genero'] = get_gen
        else:
            filtro_gen = self.request.session['genero']

        if get_pre:
            filtro_pre = get_pre
            self.request.session['prenda'] = get_pre
        else:
            filtro_pre = self.request.session['prenda']

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