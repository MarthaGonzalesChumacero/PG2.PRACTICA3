from django.db import models

# servicios/models.py
from django.db import models

class Impuesto(models.Model):
    nombre = models.CharField(max_length=200)
    sigla = models.CharField(max_length=50, blank=True, null=True)
    descripcion_general = models.TextField(blank=True, null=True)
    sujeto_activo = models.CharField(max_length=200, blank=True, null=True)
    sujeto_pasivo = models.CharField(max_length=200, blank=True, null=True)
    alicuota = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    conceptos_clave_relacionados = models.ManyToManyField('ConceptoClave', blank=True, related_name='impuestos')
    obligaciones_relacionadas = models.ManyToManyField('Obligacion', blank=True, related_name='impuestos')


    def __str__(self):
        return self.nombre
    
class Obligacion(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True, null=True)
    plazo_general = models.CharField(max_length=100, blank=True, null=True)
    requisitos_principales = models.TextField(blank=True, null=True)
    impuestos_relacionados = models.ManyToManyField(Impuesto, blank=True, related_name='obligaciones')

    def __str__(self):
        return self.nombre

class ConceptoClave(models.Model):
    termino = models.CharField(max_length=200, unique=True)
    definicion = models.TextField(blank=True, null=True)
    importancia = models.TextField(blank=True, null=True)
    como_obtenerlo = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.termino

class BeneficioCumplimiento(models.Model):
    descripcion = models.CharField(max_length=200)
    detalle = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.descripcion

class PreguntaFrecuente(models.Model):
    pregunta = models.TextField()
    respuesta = models.TextField()

    def __str__(self):
        return self.pregunta