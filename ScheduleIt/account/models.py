from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Evaluacion(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    materia = models.CharField(max_length=100)
    fecha = models.DateField()
    hora = models.TimeField()
    hora_fin = models.TimeField(null=True, blank=True)
    lugar = models.CharField(max_length=100)
    descripcion = models.TextField()
    color = models.CharField(max_length=100, null=True, blank=True)
    creado = models.DateTimeField(auto_now=False,auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True,auto_now_add=False)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.nombre
