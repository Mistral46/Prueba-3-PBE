from django.contrib import admin

# Register your models here.
from .models import Pais

#admin.site.register(Pais)

@admin.register(Pais)
class PaisAdmin(admin.ModelAdmin):
    lis_display = [ 'nombre',
                    'coloresBandera',
                    'fundacion',
                    'diaNacional',
                    'baileNacional',
                    'animalNacional',
    ]
