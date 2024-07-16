from django.db import models

class Solicitud(models.Model):
    nombre_cliente = models.CharField(max_length=100)
    tipo_reparacion = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)
    alta_eficiencia = models.BooleanField(default=False)
    descripcion_problema = models.TextField()

    def __str__(self):
        return self.nombre_cliente
# En models.py de tu app
from django.db import models
class Solicitud(models.Model):
    nombre = models.CharField(max_length=100)
    tipo_reparacion = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)
    alta_eficiencia = models.BooleanField(default=False)
    descripcion_problema = models.TextField()

    def __str__(self):
        return f'Solicitud de {self.nombre} - {self.tipo_reparacion}'