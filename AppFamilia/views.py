from django.shortcuts import render
from django.http import HttpResponse
from AppFamilia.models import Familiares
from django.template import loader

# Create your views here.

def familiares(request):
    
    familiar = Familiares(nombre='Juilia', edad=20, nacimiento='2002-2-2')
    familiar.save()

    dicc = {'nombre':['Julia', 'Mario', 'Debo'], 'edad':[20,45,40],'nacimiento':['2002-2-2','1977-3-4','1982-6-1']}

    plantilla = loader.get_template('template.html')
    documento = plantilla.render(dicc)
    
    return HttpResponse(documento)
    return HttpResponse(f'El famiilar que se llama {familiar.nombre} nació en {familiar.nacimiento}, entonces tiene {familiar.edad} años.')
    return HttpResponse(documento)
