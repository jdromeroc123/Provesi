from .models import OrdenDeCompra
from rest_framework import serializers

class OrdenDeCompraSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrdenDeCompra
        fields = '__all__'