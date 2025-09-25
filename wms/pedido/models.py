from django.db import models

from cliente.models import Cliente
# Create your models here.

class NombreEstado(models.TextChoices):
    EN_TRANSITO = 'EN_TRANSITO', 'En tránsito'
    EN_ALISTAMIENTO = 'EN_ALISTAMIENTO', 'En alistamiento'
    POR_VERIFICAR = 'POR_VERIFICAR', 'Por verificar'
    VERIFICADO = 'VERIFICADO', 'Verificado'
    RECHAZADO_VERIFICACION = 'RECHAZADO_VERIFICACION', 'Rechazado por verificación'
    EMPACADO = 'EMPACADO', 'Empacado'
    FACTURACION_PENDIENTE = 'FACTURACION_PENDIENTE', 'Facturación pendiente'
    FACTURADO = 'FACTURADO', 'Facturado'
    DESPACHADO = 'DESPACHADO', 'Despachado'
    ENTREGADO = 'ENTREGADO', 'Entregado'
    DEVUELTO = 'DEVUELTO', 'Devuelto'

class Pedido(models.Model):
    fechaCreacion = models.DateField()
    observaciones = models.TextField()
    valorTotal = models.DecimalField(max_digits=10, decimal_places=2)
    direccion = models.TextField()
    guia = models.TextField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    estado_actual = models.CharField(
        max_length=100,
        choices=NombreEstado.choices,
        default=NombreEstado.EN_TRANSITO
    )
    
    def __str__(self):
        return 'Pedido creado el {0} con un valor total de {1} en direccion a {2}'.format(self.fechaCreacion, self.valorTotal, self.direccion)
    