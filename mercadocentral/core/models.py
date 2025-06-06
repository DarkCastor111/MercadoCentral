from django.db import models
from django.contrib.auth.models import User

# Create your models here.

def custom_upload_to(instancia, nombre_fichero):
    if instancia.pk:
        antigua_instancia = Anuncio.objects.get(pk=instancia.pk)
        antigua_instancia.foto.delete()
    return 'anuncios/' + nombre_fichero

class Anuncio(models.Model):
    ESCUELA = [
        ("ESC_NIN", "Ninguna"),
        ("ESC_CHI", "Hispano Inglés")
    ]

    TIPO_PRENDA = [
        ("PRD_NIN", "Ninguno"),
        ("PRD_ALL", "Todas"),
        ("PRD_UN", "Todos Uniformes"),
        ("PRD_UN_PAN", "Pantalón Uniforme"),
        ("PRD_UN_SUE", "Suéter Uniforme"),
        ("PRD_UN_FAL", "Falda Uniforme"),
        ("PRD_UN_POL", "Polo Uniforme"),
        ("PRD_DP", "Todos Deportes"),
        ("PRD_DP_PAN", "Pantalón Deportes"),
        ("PRD_DP_BER", "Bermuda Deportes"),
        ("PRD_DP_POL", "Polo Deportes"),
        ("PRD_DP_CHQ", "Chaqueta Deportes"),
        ("PRD_DP_CHD", "Chandal completo Deportes")
    ]

    ESTADO = [
        ("EST_ALL", "Todos"),
        ("EST_NIN", "No precisado"),
        ("EST_NUEVO", "Nuevo"),
        ("EST_COMNUE", "Como nuevo"),
        ("EST_PRIM", "Primera mano"),
        ("EST_SEC", "Secunda mano"),
    ]

    GENERO = [
        ("GEN_ALL", "Todos"),
        ("GEN_MX", "Mixto"),
        ("GEN_NO", "Niño"),
        ("GEN_NA", "Niña"),
    ]   


    designacion = models.CharField(verbose_name="Designación", max_length=200)
    descripcion = models.TextField(verbose_name="Descripción")
    escuela = models.CharField(max_length=64, choices=ESCUELA, null=True)
    genero = models.CharField(max_length=64, choices=GENERO, null=True)
    estado = models.CharField(max_length=64, choices=ESTADO, null=True)
    prenda = models.CharField(max_length=64, choices=TIPO_PRENDA, null=True)
    talla = models.SmallIntegerField(null=True)
    foto = models.ImageField(upload_to=custom_upload_to, null=True, blank=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    mensajes = models.SmallIntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "anuncio"
        verbose_name_plural = "anuncios"
        ordering = ['-created', 'designacion']

    def __str__(self):
        return self.designacion
    
class Mensaje(models.Model):

    anuncio = models.ForeignKey(Anuncio, on_delete=models.CASCADE, related_name="mensajes_anuncio")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="mensajes_author")
    texto = models.TextField(verbose_name="Mensaje")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "mensaje"
        verbose_name_plural = "mensajes"
        ordering = ['-created']

    def __str__(self):
        return f'{self.created.strftime("%d/%m/%Y %H:%M")}'
