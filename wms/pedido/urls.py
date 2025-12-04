from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PedidoViewSet, PedidosPendientesViewSet

router = DefaultRouter()
router.register(r'pedidos', PedidoViewSet)
router.register(r'pedidos-pendientes', PedidosPendientesViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
