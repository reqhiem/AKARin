from django.db import models

# Create your models here.

class Documento(models.Model):
    nombre = models.CharField(max_length=30)
    tipo = models.CharField(max_length=20)
    loaded = models.DateTimeField(auto_now_add=True)
    tag = models.CharField(max_length=20)
    doc = models.FileField(upload_to='myapp/uploads/')

    class Meta:
        verbose_name = 'documento'
        verbose_name_plural = 'documentos'

    def __str__(self):
        return self.nombre
    