from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClienteViewSet
from . import views

router = DefaultRouter()
router.register(r'clientes', ClienteViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/clientes-list/', views.cliente_list, name='cliente_list'),
    path('api/clientes/<int:id>/', views.single_cliente, name='single_cliente'),
    path('api/clientes-create/', views.cliente_create, name='cliente_create'),
]
