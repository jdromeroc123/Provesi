from django.shortcuts import render
from rest_framework import viewsets
from .models import OrdenDeCompra
from .serializers import OrdenDeCompraSerializer
# Create your views here.

class OrdenDeCompraViewSet(viewsets.ModelViewSet):
    queryset=OrdenDeCompra.objects.all()
    serializer_class=OrdenDeCompraSerializer