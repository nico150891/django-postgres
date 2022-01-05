from django.http import HttpRequest
from django.http.response import HttpResponse
import datetime
from django.template import Template, Context, loader
from django.shortcuts import render

class Persona (object):

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

# def saludo(request): #primera vista

#     p2 = Persona("Marianela Dulce", "Fernandez")

#     nombre = "Nico"
#     apellido = "Leiva"
#     ahora_fecha = datetime.datetime.now()

#     # Plantilla sin parámetros
#     # doc_externo = open("/home/nico0891/django-postgres/ejemplodjango/ejemplodjango/templates/miplantilla.html")
#     # plt = Template(doc_externo.read())
#     # doc_externo.close()
#     # ctx = Context()
#     # documento = plt.render(ctx)

#     # Plantilla con parámetros
#     # doc_externo = open("/home/nico0891/django-postgres/ejemplodjango/ejemplodjango/templates/miplantilla.html")
#     # plt = Template(doc_externo.read())
#     # doc_externo.close()
#     # dicc = {"nombre_persona": nombre,
#     #         "apellido": apellido,
#     #         "fecha_ctual": ahora_fecha,
#     #         "persona_2": p2,
#     #         "temas": ["Plantillas", "Modelos", "Vistas"],
            
#     #     }
#     # ctx = Context(dicc)
#     # documento = plt.render(ctx)

#     # doc_externo = open("/home/nico0891/django-postgres/ejemplodjango/ejemplodjango/templates/miplantilla.html")
#     # plt = Template(doc_externo.read())
#     # doc_externo.close()

#     doc_externo = loader.get_template("miplantilla.html")
#     dicc = {"nombre_persona": nombre,
#             "apellido": apellido,
#             "fecha_ctual": ahora_fecha,
#             "persona_2": p2,
#             "temas": ["Plantillas", "Modelos", "Vistas"],
            
#         }
#     # ctx = Context(dicc)
#     documento = doc_externo.render(dicc)

#     return HttpResponse(documento)

def saludo(request): #primera vista

    p2 = Persona("Marianela Dulce", "Fernandez")

    nombre = "Nico"
    apellido = "Leiva"
    ahora_fecha = datetime.datetime.now()

    dicc = {"nombre_persona": nombre,
            "apellido": apellido,
            "fecha_ctual": ahora_fecha,
            "persona_2": p2,
            "temas": ["Plantillas", "Modelos", "Vistas", "Render"],
            
        }

    return render(request, "miplantilla.html", dicc)

def despedida(request): #segunda vista

    return HttpResponse("Good bye")

def give_date(request):

    date = datetime.datetime.now()

    return HttpResponse(date)

def calcula_edad(request, edad, ano):

    #dadActual = 18
    periodo = ano - 2022
    edadFutura = edad + periodo

    return HttpResponse(edadFutura)

def hija(request):

    return render(request, "hija.html")

def hija_dos(request):

    return render(request, "hijados.html")