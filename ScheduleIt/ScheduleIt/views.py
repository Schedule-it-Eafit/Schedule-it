from django.http import HttpResponse
import datetime
from django.template import Template, Context

def home(request):
    plantillaExterna = open("D:/RYZEN/Escritrio/PI1/ScheduleIt/ScheduleIt/plantillas/home.html")
    template = Template(plantillaExterna.read())
    plantillaExterna.close()
    contexto = Context()
    documento = template.render(contexto)
    return HttpResponse(documento)