from django.db import models

# Create your models here.

class Sponsor(models.Model):
    nombre = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='logos/')
    link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.nombre

class Evento(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha = models.DateField()
    imagen = models.ImageField(upload_to='eventos/')
    sponsors = models.ManyToManyField('Sponsor', blank=True, related_name='eventos')

    def __str__(self):
        return self.titulo