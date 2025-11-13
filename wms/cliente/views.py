from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Cliente 
from .serializers import ClienteSerializer
from django.contrib import messages
from django.http import JsonResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from wms.auth0backend import getRole
import json


class VendedorPermission(permissions.BasePermission):
     def has_permission(self, request, view):
        role = getRole(request)
        return role == "Vendedor"


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    permission_classes = [VendedorPermission]

@login_required
def cliente_list(request):
    role = getRole(request)
    if role != "Vendedor":
        return JsonResponse({'error': 'Unauthorized'}, status=403)
    
    clientes = list(Cliente.objects.values()) 
    return JsonResponse({'clientes': clientes})

@login_required
def single_cliente(request, id=0):
    role = getRole(request)
    if role != "Vendedor":
        return JsonResponse({'error': 'Unauthorized'}, status=403)
    try:
        cliente = Cliente.objects.values().get(id=id)
        return JsonResponse({'cliente': cliente})
    except Cliente.DoesNotExist:
        return JsonResponse({'error': 'Cliente not found'}, status=404)

@login_required
def cliente_create(request):
    role = getRole(request)
    if role != "Vendedor":
        return JsonResponse({'error': 'Unauthorized'}, status=403)
    
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            cliente = Cliente.objects.create(**data)
            return JsonResponse({'nombre': cliente.nombre, 'message': 'Cliente creado'})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    else:
        return JsonResponse({'error': 'POST method required'}, status=400)
