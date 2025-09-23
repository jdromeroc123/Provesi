from django.db import models

from producto.models import Producto
from pedido.models import Pedido

# Create your models here.

class OrdenDeCompra(models.Model):
    cantidad = models.IntegerField()
    fecha = models.DateField()
    valor = models.FloatField()
    producto = models.OneToOneField(Producto, on_delete=models.CASCADE)
    pedido = models.OneToOneField(Pedido, on_delete=models.CASCADE)
    
    def __str__(self):
        return '{0} productos por un total de {1}'.format(self.cantidad, self.valor)
