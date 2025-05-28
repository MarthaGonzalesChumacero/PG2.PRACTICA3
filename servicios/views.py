from django.shortcuts import render

# servicios/views.py

from rest_framework import viewsets
from .models import Impuesto, Obligacion, ConceptoClave, BeneficioCumplimiento, PreguntaFrecuente
from .serializers import ImpuestoSerializer, ObligacionSerializer, ConceptoClaveSerializer, BeneficioCumplimientoSerializer, PreguntaFrecuenteSerializer

class ImpuestoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Impuesto.objects.all()
    serializer_class = ImpuestoSerializer
    lookup_field = 'sigla' 

class ObligacionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Obligacion.objects.all()
    serializer_class = ObligacionSerializer

class ConceptoClaveViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ConceptoClave.objects.all()
    serializer_class = ConceptoClaveSerializer
    lookup_field = 'termino' 

class BeneficioCumplimientoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = BeneficioCumplimiento.objects.all()
    serializer_class = BeneficioCumplimientoSerializer

class PreguntaFrecuenteViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = PreguntaFrecuente.objects.all()
    serializer_class = PreguntaFrecuenteSerializer
