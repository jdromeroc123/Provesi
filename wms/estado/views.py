from django.shortcuts import render
from rest_framework import viewsets
from .models import Estado 
from .serializers import EstadoSerializer
# Create your views here.

class EstadoViewSet(viewsets.ModelViewSet):
    queryset=Estado.objects.all()
    serializer_class=EstadoSerializer