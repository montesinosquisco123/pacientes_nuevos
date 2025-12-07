from django.db import models

class Paciente(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.PositiveIntegerField()
    direccion = models.CharField(max_length=200)
    fecha_nacimiento = models.DateField()

    def __str__(self):
        return self.nombre
