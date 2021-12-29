from django.http import HttpRequest
from django.http.response import HttpResponse

def saludo(request): #primera vista

    return HttpResponse("Hola mundo vista")

def despedida(request): #segunda vista

    return HttpResponse("Good bye")