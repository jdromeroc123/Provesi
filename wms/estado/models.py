from django.db import models

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



class Estado(models.Model):
    estado = models.CharField(max_length=100, choices=NombreEstado.choices)
    fecha = models.DateField()
    
    def __str__(self):
        return 'En estado {0} desde la fecha {1}'.format(self.estado, self.fecha)
    