from django.urls import path
from .views import *

urlpatterns = [
    path('olamundo/', olamundo, name='olamundo'),
    path('instituicao/', instituicao, name='instituicao'),
    path('materias/', materias, name='materias'),
    path('receber_1/', receber_1, name='receber_1'),
    path('areas_lista/', areas_lista, name='areas_lista'),
    path('publico_lista/', publico_lista, name='publico_lista'),
]