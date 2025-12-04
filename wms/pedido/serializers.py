from rest_framework_mongoengine.serializers import DocumentSerializer
from .models import Pedido
from .subset import PedidosPendientes

class PedidoSerializer(DocumentSerializer):
    class Meta:
        model = Pedido
        fields = '__all__'

class PedidosPendientesSerializer(DocumentSerializer):
    class Meta:
        model = PedidosPendientes
        fields = '__all__'