from django.contrib import admin

# servicios/admin.py
from django.contrib import admin
from .models import Impuesto, Obligacion, ConceptoClave, BeneficioCumplimiento, PreguntaFrecuente

admin.site.register(Impuesto)
admin.site.register(Obligacion)
admin.site.register(ConceptoClave)
admin.site.register(BeneficioCumplimiento)
admin.site.register(PreguntaFrecuente)