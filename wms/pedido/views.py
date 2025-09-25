from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Pedido 
from .serializers import PedidoSerializer
# Create your views here.

class PedidoViewSet(viewsets.ModelViewSet):
    queryset=Pedido.objects.all()
    serializer_class=PedidoSerializer
    
    @action(detail=False, methods=['get'], url_path='pendientes')
    def pedidos_pendientes(self, request):
        estados_finales = ['DESPACHADO', 'ENTREGADO', 'DEVUELTO']
        pedidos = Pedido.objects.exclude(estado_actual__in=estados_finales)
        serializer = self.get_serializer(pedidos, many=True)
        return Response(serializer.data)