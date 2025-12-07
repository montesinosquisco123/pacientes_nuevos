from django.db import models

class Paciente(models.Model):
    nombre = models.CharField(max_length=100)
    rut = models.CharField(max_length=12)
    fecha_nacimiento = models.DateField()
    telefono = models.CharField(max_length=15)

    def __str__(self):
        return self.nombre
