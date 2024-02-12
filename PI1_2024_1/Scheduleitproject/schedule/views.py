from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    #return HttpResponse('<div><body><h1>Bienvenido a Schedule-it</h1><p><b>En esta pagina podras asignar tus examenes y materias.</b></p><button><b>Materias</b></button></body></div>')
    return render(request, 'home.html')