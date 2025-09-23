from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OrdenDeCompraViewSet

router = DefaultRouter()
router.register(r'ordenes-de-compra', OrdenDeCompraViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
