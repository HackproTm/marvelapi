from django.db import models

# Create your models here.


class Peliculas(models.Model):
    titulo = models.CharField(max_length=250, blank=False, default=None)

    fecha = models.IntegerField(blank=False)

    clasificacion = models.CharField(max_length=3)

    duracion = models.IntegerField()

    genero = models.CharField(max_length=150)

    director = models.CharField(max_length=150)

    actores = models.CharField(max_length=800)

    sipnosis = models.TextField()

    idioma = models.CharField(max_length=50)

    pais = models.CharField(max_length=50)

    caratula = models.ImageField()
