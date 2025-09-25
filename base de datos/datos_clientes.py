import requests
from faker import Faker
import random

API_URL = "http://localhost:8080/api/clientes/" 
TOTAL_CLIENTES = 1000

fake = Faker('es_ES')  

def generar_cliente():
    return {
        "nombre": fake.word().capitalize() + " " + fake.color_name(),
        "telefono": fake.phone_number(),
        "correo": fake.email()
    }

def cargar_clientes(url):
    for i in range(TOTAL_CLIENTES):
        cliente = generar_cliente()
        response = requests.post(url, json=cliente)

        if response.status_code == 201:
            print(f"[{i+1}] Cliente creado: {cliente['nombre']}")
        else:
            print(f"[{i+1}] Error ({response.status_code}): {response.text}")