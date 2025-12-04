from mongoengine import (
    Document,
    DateField,
    StringField,
    DecimalField
)
from .subset import PedidosPendientes

class NombreEstado:
    EN_TRANSITO = 'EN_TRANSITO'
    EN_ALISTAMIENTO = 'EN_ALISTAMIENTO'
    POR_VERIFICAR = 'POR_VERIFICAR'
    VERIFICADO = 'VERIFICADO'
    RECHAZADO_VERIFICACION = 'RECHAZADO_VERIFICACION'
    EMPACADO = 'EMPACADO'
    FACTURACION_PENDIENTE = 'FACTURACION_PENDIENTE'
    FACTURADO = 'FACTURADO'
    DESPACHADO = 'DESPACHADO'
    ENTREGADO = 'ENTREGADO'
    DEVUELTO = 'DEVUELTO'

    CHOICES = [
        EN_TRANSITO,
        EN_ALISTAMIENTO,
        POR_VERIFICAR,
        VERIFICADO,
        RECHAZADO_VERIFICACION,
        EMPACADO,
        FACTURACION_PENDIENTE,
        FACTURADO,
        DESPACHADO,
        ENTREGADO,
        DEVUELTO,
    ]


class Pedido(Document):
    fechaCreacion = DateField(required=True)
    observaciones = StringField()
    valorTotal = DecimalField(precision=2, required=True)
    direccion = StringField()
    guia = StringField()
    cliente = StringField()
    estado_actual = StringField(
        choices=NombreEstado.CHOICES,
        default=NombreEstado.EN_TRANSITO
    )

    meta = {
        'collection': 'pedidos',
        'ordering': ['-fechaCreacion']
    }

    def __str__(self):
        return f'Pedido del {self.fechaCreacion} por {self.valorTotal} hacia {self.direccion}'

    def save(self, *args, **kwargs):
        """
        Sobrescribe save para mantener sincronizado PedidosPendientes.
        """
        # Guardamos el pedido primero
        super().save(*args, **kwargs)

        estados_pendientes = [
            NombreEstado.EN_TRANSITO,
            NombreEstado.EN_ALISTAMIENTO,
            NombreEstado.POR_VERIFICAR,
            NombreEstado.VERIFICADO,
            NombreEstado.RECHAZADO_VERIFICACION,
            NombreEstado.EMPACADO,
            NombreEstado.FACTURACION_PENDIENTE,
            NombreEstado.FACTURADO
        ]

        if self.estado_actual in estados_pendientes:

            PedidosPendientes.objects.update_one(
                pedido=self,
                set__pedido=self,
                set__fechaCreacion=self.fechaCreacion,
                set__estado_actual=self.estado_actual,
                set__valorTotal=self.valorTotal,
                set__cliente=self.cliente,
                upsert=True 
            )
        else:
        
            PedidosPendientes.objects(pedido=self).delete()