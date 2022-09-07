from contextvars import Context
from multiprocessing import context
from pipes import Template
from django.http import HttpResponse
from django.http import HttpRequest
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render
from datetime import datetime

class Persona(object):

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido



def saludo(request): #primera vista    

    p1 = Persona("Juanes", "Perez")
    fecha_actual = datetime.now()
    temass = ["Plantillas","Modelos","Formularios","Vistas","Despliegue"]
    diccionario = {"nombre_persona":p1.nombre, "apellido_persona":p1.apellido.upper(), "ahora":fecha_actual.strftime('%d/%m/%Y'), "temas":temass}
    # doc_externo = open("D:/02-Projects/Django/Fundamentos/proyecto1/proyecto1/plantillas/inicio.html")
    #plt = Template(doc_externo.read())
    # doc_externo.close()
    # doc_externo = get_template('inicio.html')    
    # ctx = Context({"nombre_persona":p1.nombre, "apellido_persona":p1.apellido.upper(), "ahora":fecha_actual.strftime('%d/%m/%Y'), "temas":temass})
    # documento = doc_externo.render({"nombre_persona":p1.nombre, "apellido_persona":p1.apellido.upper(), "ahora":fecha_actual.strftime('%d/%m/%Y'), "temas":temass})

    # return HttpResponse(documento)
    return render(request,"inicio.html",diccionario)

def despedida(request):
    return HttpResponse("Bye bitches")
 
def damefecha(request):
    fecha_actual = datetime.datetime.now()
    documento = """<html>
    <body>
    <h2>
    Fecha y hora actuales %s
    </h2>
    </body>
    </html>""" % fecha_actual

    return HttpResponse(documento)

def calcula_edad(request, anno,):#asi es como se hace una funcion con 1 parametro
    edadActual = 34
    periodo=anno-2022
    edadFutura = edadActual + periodo
    documento ="""
    <html>
    <body>
    <h3>
    En el año %s tendras %s años""" %(anno,edadFutura)
    return HttpResponse(documento)

def calcula_edad2(request, anno, edad):#asi es como se hace una funcion con 1 parametro
    periodo=anno-2022
    edadFutura = edad + periodo
    documento ="""
    <html>
    <body>
    <h3>
    En el año %s tendras %s años""" %(anno,edadFutura)
    return HttpResponse(documento)
