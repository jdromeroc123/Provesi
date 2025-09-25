import requests
from faker import Faker
import random
from datetime import timedelta, date

API_URL = "http://localhost:8080/api/estados/"  # Cambia esta URL si tu endpoint es diferente
TOTAL_ESTADOS = 18000

fake = Faker('es_ES')

# Lista de estados válidos según tu enumeración
ESTADOS_VALIDOS = [
    'EN_TRANSITO',
    'EN_ALISTAMIENTO',
    'POR_VERIFICAR',
    'VERIFICADO',
    'RECHAZADO_VERIFICACION',
    'EMPACADO',
    'FACTURACION_PENDIENTE',
    'FACTURADO',
    'DESPACHADO',
    'ENTREGADO',
    'DEVUELTO'
]

def generar_estado():
    fecha_inicio = date.today() - timedelta(days=365)
    fecha_random = fecha_inicio + timedelta(days=random.randint(0, 365))

    return {
        "estado": random.choice(ESTADOS_VALIDOS),
        "fecha": fecha_random.isoformat(),
        "pedido": random.randint(1,5000)
    }

def cargar_estados(url):
    for i in range(TOTAL_ESTADOS):
        estado = generar_estado()
        response = requests.post(url, json=estado)

        if response.status_code == 201:
            print(f"[{i+1}] Estado creado: {estado['estado']} en {estado['fecha']}")
        else:
            print(f"[{i+1}] Error ({response.status_code}): {response.text}")