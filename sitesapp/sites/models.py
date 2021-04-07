from django.db import models

# Create your models here.
class Rol(models.Model):
    descripcion = models.CharField(max_length=100)
    def __str__(self):
        return self.descripcion

class Miembro(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    rol = models.ForeignKey(Rol,on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"