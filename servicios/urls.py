# servicios/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    ImpuestoViewSet,
    ObligacionViewSet,
    ConceptoClaveViewSet,
    BeneficioCumplimientoViewSet,
    PreguntaFrecuenteViewSet
)

router = DefaultRouter()
router.register(r'impuestos', ImpuestoViewSet)
router.register(r'obligaciones', ObligacionViewSet)
router.register(r'conceptos-clave', ConceptoClaveViewSet)
router.register(r'beneficios', BeneficioCumplimientoViewSet)
router.register(r'preguntas-frecuentes', PreguntaFrecuenteViewSet)

urlpatterns = [
    path('', include(router.urls)),  # Es importante usar '' aquí para que coincida correctamente con /api/
]

