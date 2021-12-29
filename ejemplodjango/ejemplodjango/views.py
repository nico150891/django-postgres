from django.http import HttpRequest
from django.http.response import HttpResponse
import datetime

def saludo(request): #primera vista

    return HttpResponse("Hola mundo vista")

def despedida(request): #segunda vista

    return HttpResponse("Good bye")

def giveDate(request):

    date = datetime.datetime.now()

    return HttpResponse(date)

def calculaEdad(request, edad, ano):

    #dadActual = 18
    periodo = ano - 2022
    edadFutura = edad + periodo

    return HttpResponse(edadFutura)