from rest_framework import serializers
from .models import Impuesto, Obligacion, ConceptoClave, BeneficioCumplimiento, PreguntaFrecuente

class ConceptoClaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConceptoClave
        fields = '__all__'

class ObligacionSerializer(serializers.ModelSerializer):
    impuestos_relacionados = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Obligacion
        fields = '__all__'

class ImpuestoSerializer(serializers.ModelSerializer):
    conceptos_clave_relacionados = ConceptoClaveSerializer(many=True, read_only=True)
    obligaciones_relacionadas = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Impuesto
        fields = '__all__'

class BeneficioCumplimientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = BeneficioCumplimiento
        fields = '__all__'

class PreguntaFrecuenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = PreguntaFrecuente
        fields = '__all__'