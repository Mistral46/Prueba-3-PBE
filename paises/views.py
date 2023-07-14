#from django.shortcuts import render
from rest_framework import viewsets
from .serializer import PaisSerializer
from .models import Pais
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status


# Create your views here.
class PaisViewSet (viewsets.ModelViewSet):
    queryset = Pais.objects.all() #Obtener todos los registros de la tabla
    serializer_class = PaisSerializer #Clase serializadora

 #Listar Datos
@api_view(['GET'])
def getPais(request):
    paises= Pais.objects.all()
    serializer = PaisSerializer(paises, many = True)
    return Response(serializer.data)

#Grabar Datos
@api_view(['POST'])
def postPais(request):
    data = request.data
    pais = Pais.objects.create(
        nombre = data['nombre'],
        colBandera = data['coloresBandera'],
        fundacion = data['fundacion'],
        diaNacional = data['diaNacional'],
        baileNacional = data['baileNacional'],
        animalNacional = data['animalNacional'],
    )
    serializer = PaisSerializer(pais, many = False)
    return Response(serializer.data)

#Actualizar Datos
@api_view(['PUT'])
def updatePais(request):
    data = request.data
    pais = Pais.objects.get(id = data['id'])
    serializer = PaisSerializer(instance=pais, data = data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

#Eliminar Datos
@api_view(['DELETE'])
def  deletePais(request):
    data = request.data
    pais= Pais.objects.filter(id = data['id'])
    pais.delete()
    respuesta = {'message': 'Eliminación exitosa'}
    return Response(respuesta,status= status.HTTP_204_NO_CONTENT)   
   