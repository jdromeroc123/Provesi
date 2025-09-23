from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EstadoViewSet

router = DefaultRouter()
router.register(r'estados', EstadoViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
