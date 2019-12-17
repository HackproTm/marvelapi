from django.shortcuts import render
from peliculas.models import Peliculas
from peliculas.serializers import PeliculasSerializer
from rest_framework import viewsets


class PeliculasViewSet(viewsets.ModelViewSet):
    queryset = Peliculas.objects.all()

    serializer_class = PeliculasSerializer
