from mongoengine import (
    Document,
    DateField,
    StringField,
    DecimalField
)

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
