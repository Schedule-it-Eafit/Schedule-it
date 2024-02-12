from django.db import models

# Create your models here.

class Usuario(models.Model):
    IdUsuario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    usuario = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def NombreCompleto(self):
        return "{} {}".format(self.apellido, self.nombre)

    def __str__(self):
        return self.NombreCompleto()
    
class Materia(models.Model):
    IdMateria = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    def __str__(self):
        return self.nombre
    
class PactoPedagogico(models.Model):
    IdPactoPedagogico = models.AutoField(primary_key=True)
    IdMateria = models.ForeignKey(Materia, on_delete=models.CASCADE)

class Evaluacion(models.Model):
    IdEvaluacion = models.AutoField(primary_key=True)
    Tipo = models.CharField(max_length=50)
    fecha = models.DateField()
    porcentaje = models.IntegerField()
    temas = models.CharField(max_length=150)
    IdMateria = models.ForeignKey(Materia, on_delete=models.CASCADE)
    def __str__(self):
        return self.Tipo