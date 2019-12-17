from personajes.models import Personajes
from rest_framework import serializers


class PersonajesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personajes

        fields = ("id", "nombre", "nombre_real", "foto", "sexo")
