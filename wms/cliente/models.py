from django.db import models

# Create your models here.

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.TextField()
    correo = models.TextField()
    
    def __str__(self):
        return '{}'.format(self.nombre)
    