from django.db import models

# Create your models here.


class Personajes(models.Model):
    nombre = models.CharField(max_length=128, blank=False, default=None)

    nombre_real = models.CharField(max_length=128)

    foto = models.ImageField()

    sexo = models.BooleanField()
