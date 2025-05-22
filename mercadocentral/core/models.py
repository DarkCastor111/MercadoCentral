from django.db import models

# Create your models here.

class Anuncio(models.Model):
    ESCUELA = {
        "ESC_NIN" : "Ninguna",
        "ESC_CHI" : "Ispano Ingles"
    }

    TIPO_PRENDA = {
        "PRD_NIN" : "Ninguno",
        "PRD_UN_PAN" : "Pantalón",
        "PRD_UN_SUE" : "Suéter",
        "PRD_UN_FAL" : "Falda",
        "PRD_UN_POL" : "Polo",
        "PRD_DP_PAN" : "Pantalón",
        "PRD_DP_BER" : "Bermuda",
        "PRD_DP_POL" : "Polo",
        "PRD_DP_CHQ" : "Chaqueta",
        "PRD_DP_CHD" : "Chandal completo",
    }

    ESTADO = {
        "EST_NIN" : "No precisado",
        "EST_NUEVO" : "Nuevo",
        "EST_COMNUE" : "Como nuevo",
        "EST_PRIM" : "Primera mano",
        "EST_SEC" : "Secunda mano",
    }

    GENERO = {
        "GEN_AMB" : "Ambos",
        "GEN_NO" : "Niño",
        "GEN_NA" : "Niña",
    }   


    designacion = models.CharField(verbose_name="Designación", max_length=200)
    descripcion = models.TextField(verbose_name="Descripción")
    escuela = models.CharField(max_length=64, choices=ESCUELA, null=True)
    genero = models.CharField(max_length=64, choices=GENERO, null=True)
    estado = models.CharField(max_length=64, choices=ESTADO, null=True)
    prenda = models.CharField(max_length=64, choices=TIPO_PRENDA, null=True)
    foto = models.URLField(max_length=254, null=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "anuncio"
        verbose_name_plural = "anuncios"
        ordering = ['-created', 'designacion']

    def __str__(self):
        return self.designacion