import requests
from faker import Faker
import random
from datetime import timedelta, date

TOTAL_PEDIDOS_ALEATORIOS = 5500
TOTAL_PEDIDOS_PENDIENTES = 320

fake = Faker('es_ES')

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

ESTADOS_PENDIENTES = [
    'EN_TRANSITO',
    'EN_ALISTAMIENTO',
    'POR_VERIFICAR',
    'VERIFICADO',
    'RECHAZADO_VERIFICACION',
    'EMPACADO',
    'FACTURACION_PENDIENTE',
    'FACTURADO',
]

def generar_pedido_aleatorio(cliente_id):
    fecha = date.today() - timedelta(days=random.randint(0, 365))
    return {
        "fechaCreacion": fecha.isoformat(),
        "observaciones": fake.sentence(nb_words=10),
        "valorTotal": round(random.uniform(100, 10000), 2),
        "direccion": fake.address(),
        "guia": fake.bothify(text="GUIA-####-????"),
        "cliente": cliente_id,
        "estado_actual": random.choice(ESTADOS_VALIDOS)
    }

def cargar_pedidos_aleatorios(url):
    for i in range(TOTAL_PEDIDOS_ALEATORIOS):
        cliente_id = random.randint(102, 1101)
        pedido = generar_pedido_aleatorio(cliente_id)

        response = requests.post(url, json=pedido)

        if response.status_code == 201:
            print(f"[{i}] Pedido creado en estado {pedido['estado_actual']} el {pedido['fechaCreacion']}")
        else:
            print(f"[{i}] Error al crear pedido: {response.status_code} - {response.text}")

def generar_pedido_pendiente(cliente_id):
    fecha = date.today() - timedelta(days=random.randint(0, 365))
    return {
        "fechaCreacion": fecha.isoformat(),
        "observaciones": fake.sentence(nb_words=10),
        "valorTotal": round(random.uniform(100, 10000), 2),
        "direccion": fake.address(),
        "guia": fake.bothify(text="GUIA-####-????"),
        "cliente": cliente_id,
        "estado_actual": random.choice(ESTADOS_PENDIENTES)
    }

def cargar_pedidos_pendientes(url):
    for i in range(TOTAL_PEDIDOS_PENDIENTES):
        cliente_id = random.randint(102, 1101)
        pedido = generar_pedido_pendiente(cliente_id)

        response = requests.post(url, json=pedido)

        if response.status_code == 201:
            print(f"[{i}] Pedido creado en estado {pedido['estado_actual']} el {pedido['fechaCreacion']}")
        else:
            print(f"[{i}] Error al crear pedido: {response.status_code} - {response.text}")
