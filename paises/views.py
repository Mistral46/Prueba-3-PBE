#from django.shortcuts import render
from rest_framework import viewsets
from .serializer import PaisSerializer
from .models import Pais

# Create your views here.
class PaisViewSet (viewsets.ModelViewSet):
    queryset = Pais.objects.all() #Obtener todos los registros de la tabla
    serializer_class = PaisSerializer #Clase serializadora