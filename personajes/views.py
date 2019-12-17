from django.shortcuts import render
from personajes.models import Personajes
from personajes.serializers import PersonajesSerializer
from rest_framework import viewsets


class PersonajesViewSet(viewsets.ModelViewSet):
    queryset = Personajes.objects.all()

    serializer_class = PersonajesSerializer
