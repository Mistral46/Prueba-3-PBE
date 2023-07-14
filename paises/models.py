from django.db import models

# Create your models here.
class Pais (models.Model):
    nombre = models.CharField(max_length=100)
    colBandera = models.CharField(max_length=100)
    fundacion = models.DateField()
    diaNacional = models.DateField()
    baileNacional = models.CharField(max_length=100)
    animalNacional = models.CharField(max_length=100)

