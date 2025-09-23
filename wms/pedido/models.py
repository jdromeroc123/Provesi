from django.db import models

from cliente.models import Cliente
from estado.models import Estado

# Create your models here.

class Pedido(models.Model):
    fechaCreacion = models.DateField()
    observaciones = models.TextField()
    valorTotal = models.DecimalField(max_digits=10, decimal_places=2)
    direccion = models.TextField()
    guia = models.TextField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)    
    
    def __str__(self):
        return 'Pedido creado el {0} con un valor total de {1} en direccion a {2}'.format(self.fechaCreacion, self.valorTotal, self.direccion)
    