from rest_framework import serializers
from .models import Impuesto, Obligacion, ConceptoClave, BeneficioCumplimiento, PreguntaFrecuente

class ImpuestoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Impuesto
        fields = '__all__'

class ObligacionSerializer(serializers.ModelSerializer):
    impuesto = ImpuestoSerializer(read_only=True)  

    class Meta:
        model = Obligacion
        fields = '__all__'
        depth = 1  

class ConceptoClaveSerializer(serializers.ModelSerializer):
    impuesto = ImpuestoSerializer(read_only=True)

    class Meta:
        model = ConceptoClave
        fields = '__all__'
        depth = 1

class BeneficioCumplimientoSerializer(serializers.ModelSerializer):
    impuesto = ImpuestoSerializer(read_only=True)

    class Meta:
        model = BeneficioCumplimiento
        fields = '__all__'
        depth = 1

class PreguntaFrecuenteSerializer(serializers.ModelSerializer):
    impuesto = ImpuestoSerializer(read_only=True)

    class Meta:
        model = PreguntaFrecuente
        fields = '__all__'
        depth = 1
