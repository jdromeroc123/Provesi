import requests
from faker import Faker
import random

TOTAL_PRODUCTOS = 1000

fake = Faker('es_ES')  

def generar_producto():
    return {
        "nombre": fake.unique.word().capitalize() + " " + fake.color_name(),
        "descripcion": fake.sentence(nb_words=12),
        "precioUnitario": round(random.uniform(10.00, 500.00), 2),
        "cantidadDisponible": random.randint(1, 200),
        "volumen": round(random.uniform(0.1, 5.0), 2)
    }

def cargar_productos(url):
    for i in range(TOTAL_PRODUCTOS):
        producto = generar_producto()
        response = requests.post(url, json=producto)

        if response.status_code == 201:
            print(f"[{i+1}] Producto creado: {producto['nombre']}")
        else:
            print(f"[{i+1}] Error ({response.status_code}): {response.text}")