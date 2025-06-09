from django.db import models
from django.contrib.auth.models import User

from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile
import os


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
        ("PRD_ALL", "Multi"),
        ("PRD_POL", "Polo"),
        ("PRD_JER", "Jersey"),
        ("PRD_FAL", "Falda"),
        ("PRD_PAN", "Pantalón"),
        ("PRD_CHD", "Chandal"),
        ("PRD_BER", "Bermuda"),
        ("PRD_BAB", "Babi"),
    ]

    ESTADO = [
        ("EST_ALL", "No precisado"),
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

    MATERIA = [
        ("MAT_ALL", "Todos"),
        ("MAT_MZ", "Mezcla"),
        ("MAT_AG", "100% Algodon o Lana"),
        ("MAT_SY", "100% Syntetico"),
    ]

    TALLA = [
        ("TAL_ALL", "No precisado"),
        ("74", "00"),
        ("78", "0"),
        ("82", "1"),
        ("98", "2"),
        ("108", "4"),
        ("118", "6"),
        ("128", "8"),
        ("140", "10"),
        ("152", "12"),
        ("164", "14"),
        ("170", "16 / S / 2A"),
        ("178", "18 / M / 3A"),
        ("184", "20 / L / 4A"),
        ("188", "22 / XL / 5A"),
        ("192", "24 / XXL / 6A"),
    ]
  



    designacion = models.CharField(verbose_name="Designación", max_length=200)
    descripcion = models.TextField(verbose_name="Descripción")
    escuela = models.CharField(max_length=64, choices=ESCUELA, null=True, blank=True)
    # genero = models.CharField(max_length=64, choices=GENERO, null=True, blank=True)
    estado = models.CharField(max_length=64, choices=ESTADO, null=True, blank=True)
    prenda = models.CharField(max_length=64, choices=TIPO_PRENDA)
    materia = models.CharField(max_length=64, choices=MATERIA, null=True, blank=True)
    talla = models.CharField(max_length=64, choices=TALLA)
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
    
    def save(self, *args, **kwargs):
        # Save the instance first to get a file path
        super().save(*args, **kwargs)

        # Tratamiento de la foto
        if self.foto and self.foto.size > 200000:
            try:
                img = Image.open(self.foto.path)
                nombre_fichero = os.path.splitext(os.path.basename(self.foto.name))[0] + ".jpg"

                # Conversión a RGB (para PNG, etc.)
                if img.mode != 'RGB':
                    img = img.convert('RGB')
                # Resize or compress as needed (optional: resize here)
                # img = img.resize((desired_width, desired_height))

                # Save to BytesIO as JPEG with 80% quality
                buffer = BytesIO()
                img.save(buffer, format='JPEG', quality=80)
                buffer.seek(0)

                # Replace the original file
                self.foto.save(
                    nombre_fichero,
                    ContentFile(buffer.read()),
                    save=False
                )
                buffer.close()
                super().save(*args, **kwargs)  # Save again to update the file
            except Exception as e:
                # Optionally log the error
                pass
    
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
