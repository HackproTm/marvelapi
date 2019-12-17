from peliculas.models import Peliculas
from rest_framework import serializers


class PeliculasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Peliculas

        fields = ("id", "titulo", "fecha", "clasificacion", "duracion", "genero", "director", "actores", "sipnosis",
                  "idioma", "pais", "caratula")
