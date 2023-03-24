from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def sumar(request , valor1 , valor2):
    resultado = valor1 + valor2
    return  HttpResponse("el resultado es : %s " %resultado)

