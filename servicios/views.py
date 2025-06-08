# servicios/views.py
from rest_framework import viewsets, filters
from .models import Impuesto, Obligacion, ConceptoClave, BeneficioCumplimiento, PreguntaFrecuente
from .serializers import (
    ImpuestoSerializer,
    ObligacionSerializer,
    ConceptoClaveSerializer,
    BeneficioCumplimientoSerializer,
    PreguntaFrecuenteSerializer
)

class ImpuestoViewSet(viewsets.ModelViewSet):
    queryset = Impuesto.objects.all()
    serializer_class = ImpuestoSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['nombre']
    ordering_fields = ['nombre']

class ObligacionViewSet(viewsets.ModelViewSet):
    queryset = Obligacion.objects.all()
    serializer_class = ObligacionSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['nombre', 'descripcion']
    ordering_fields = ['nombre']

class ConceptoClaveViewSet(viewsets.ModelViewSet):
    queryset = ConceptoClave.objects.all()
    serializer_class = ConceptoClaveSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['termino', 'definicion']
    ordering_fields = ['termino']

class BeneficioCumplimientoViewSet(viewsets.ModelViewSet):
    queryset = BeneficioCumplimiento.objects.all()
    serializer_class = BeneficioCumplimientoSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['nombre', 'descripcion']
    ordering_fields = ['nombre']

class PreguntaFrecuenteViewSet(viewsets.ModelViewSet):
    queryset = PreguntaFrecuente.objects.all()
    serializer_class = PreguntaFrecuenteSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['pregunta', 'respuesta']
    ordering_fields = ['pregunta']

