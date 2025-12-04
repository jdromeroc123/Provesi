from mongoengine import Document, StringField, ReferenceField, DateField, DecimalField
from .models import Pedido
from .models import NombreEstado

class PedidosPendientes(Document):
    pedido = ReferenceField(Pedido, required=True, unique=True)
    fechaCreacion = DateField(required=True)
    estado_actual = StringField(choices=NombreEstado.CHOICES)
    valorTotal = DecimalField(precision=2, required=True)
    cliente = StringField(required=True)

    meta = {
        'collection': 'pedidos_pendientes',
        'indexes': [
            'fechaCreacion',
            'estado_actual',
            'cliente'
        ]
    }