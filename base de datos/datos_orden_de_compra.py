import requests
from faker import Faker
import random
from datetime import timedelta, date

TOTAL_ORDENES = 20000
fake = Faker('es_ES')

def generar_orden():
    fecha = date.today() - timedelta(days=random.randint(0, 365))
    return {
        "cantidad": random.uniform(5000, 100000),
        "valor": round(random.uniform(5000, 100000), 2),
        "pedido": random.randint(1, 6000)
    }

def cargar_ordenes(url):
    for i in range(TOTAL_ORDENES):
        orden = generar_orden()
        response = requests.post(url, json=orden)

        if response.status_code == 201:
            print(f"[{i}] Orden creada por valor de {orden['valor']}")
        else:
            print(f"[{i}] Error al crear orden: {response.status_code} - {response.text}")