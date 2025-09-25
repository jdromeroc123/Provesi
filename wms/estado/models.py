from django.db import models
from pedido.models import Pedido, NombreEstado

# Create your models here.


class Estado(models.Model):
    estado = models.CharField(max_length=100, choices=NombreEstado.choices)
    fecha = models.DateField()
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    
    def __str__(self):
        return 'En estado {0} desde la fecha {1}'.format(self.estado, self.fecha)
    