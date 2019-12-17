from django.contrib import admin
from django.urls import path, include
from peliculas.views import PeliculasViewSet
from personajes.views import PersonajesViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('personajes', PersonajesViewSet)
router.register('peliculas', PeliculasViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
