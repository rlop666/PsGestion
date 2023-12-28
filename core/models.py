#from django.db import models

# Create your models here.
from django.db import models

class Direccion(models.Model):
    calleynumero = models.CharField(max_length=200)
    cp = models.IntegerField()
    localidad = models.CharField(max_length=100)
    provincia = models.CharField(max_length=100)

class PrecioSesion(models.Model):
    fechaInicio = models.DateField()
    precio = models.IntegerField()

class Paciente(models.Model):
    dni = models.CharField(max_length=15)
    nombre = models.CharField(max_length=100)
    apellido1 = models.CharField(max_length=100)
    apellido2 = models.CharField(max_length=100)
    direccion = models.JSONField()
    precioSesion = models.JSONField()
    estadoCivil = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    telefono = models.CharField(max_length=20)
    fechaAlta = models.DateField(auto_now=True, auto_now_add=False)
    fechaNacimiento = models.DateField()