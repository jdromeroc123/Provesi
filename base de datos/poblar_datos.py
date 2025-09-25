from datos_productos import cargar_productos
from datos_clientes import cargar_clientes
from datos_pedido import cargar_pedidos_aleatorios, cargar_pedidos_pendientes
from datos_orden_de_compra import cargar_ordenes
from datos_estado import cargar_estados

IP = "localhost"
PRODUCTOS_URL = f"http://{IP}:8080/api/productos/"
CLIENTES_URL = f"http://{IP}:8080/api/clientes/"
PEDIDOS_URL = f"http://{IP}:8080/api/pedidos/"
ORDENES_URL = f"http://{IP}:8080/api/ordenes-de-compra/"
ESTADOS_URL = f"http://{IP}:8080/api/estados/"

#cargar_productos(PRODUCTOS_URL)
#cargar_clientes(CLIENTES_URL)
#cargar_pedidos_aleatorios(PEDIDOS_URL)
#cargar_pedidos_pendientes(PEDIDOS_URL)
#cargar_ordenes(ORDENES_URL)
#cargar_estados(ESTADOS_URL)
