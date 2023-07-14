from rest_framework import serializers
from paises.models import Pais

class PaisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pais
        fields = [  'nombre',
                    'coloresBandera',
                    'fundacion',
                    'diaNacional',
                    'baileNacional',
                    'animalNacional',
        ]
