from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("Desde la vista encuestas!!!")

def detalle(request ):
    return HttpResponse("hola ,esats en detalle")


def resultados(request, pregunta_id):
    response = "Estas viendo los rasdfasdfasdfesultado de la pregunta %s."
    return HttpResponse(response % pregunta_id)

def votar(request, pregunta_id):
    return HttpResponse("Estas votasdfasdfasdfasdfasdfando por la pregunta %s." % pregunta_id)


def hola(request):
    return HttpResponse("hola hola hola")














