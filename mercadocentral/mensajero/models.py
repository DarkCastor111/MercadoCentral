from django.db import models
from django.contrib.auth.models import User
from core.models import Anuncio

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    contenido = models.TextField(verbose_name="Post")
    fecha_emision = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")

    class Meta():
        verbose_name = "post"
        verbose_name_plural = "posts"
        ordering = ['-fecha_emision']

    def __str__(self):
        return f'{self.author} el {self.fecha_emision.strftime("%d/%m/%Y %H:%M")}'
    
class Hilo(models.Model):
    anuncio = models.ForeignKey(Anuncio, on_delete=models.CASCADE, related_name="hilos_anuncio")
    propietario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='hilos_activos_prop')
    interesado = models.ForeignKey(User, on_delete=models.CASCADE, related_name='hilos_activos_inter')
    posts = models.ManyToManyField(Post)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    
    # objects = HiloManager()

    class Meta:
        ordering = ['-fecha_modificacion']
