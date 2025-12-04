from rest_framework_mongoengine.viewsets import ModelViewSet
from .models import Pedido
from .subset import PedidosPendientes
from .serializers import PedidoSerializer, PedidosPendientesSerializer


class PedidoViewSet(ModelViewSet):
    """
    CRUD completo para Pedido usando MongoEngine
    """
    lookup_field = 'id'   # Para que use el ObjectId de Mongo
    serializer_class = PedidoSerializer
    queryset = Pedido.objects.all()


class PedidosPendientesViewSet(ModelViewSet):
    """
    Endpoints optimizados para leer datos rápidos usando el subset pattern
    """
    lookup_field = 'id'
    serializer_class = PedidosPendientesSerializer
    queryset = PedidosPendientes.objects.all()