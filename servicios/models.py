from django.db import models

class Impuesto(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre del impuesto", db_index=True)
    descripcion = models.TextField(blank=True, null=True, verbose_name="Descripción")

    def __str__(self):
        return self.nombre

class ConceptoClave(models.Model):
    termino = models.CharField(max_length=100, verbose_name="Término clave", db_index=True)
    definicion = models.TextField(verbose_name="Definición", default="Definición no disponible")  # Se agregó default
    importancia = models.TextField(blank=True, null=True, verbose_name="Importancia")
    como_obtenerlo = models.TextField(blank=True, null=True, verbose_name="Cómo obtenerlo")
    url_fuente = models.URLField(blank=True, null=True, verbose_name="Fuente externa")
    impuesto = models.ForeignKey(Impuesto, on_delete=models.PROTECT, related_name='conceptos_clave', default=1)  # Se agregó default=1

    def __str__(self):
        return f"{self.termino[:50]}..." if len(self.termino) > 50 else self.termino

class Obligacion(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre de la obligación", db_index=True)
    descripcion = models.TextField(verbose_name="Descripción", default="Sin descripción disponible")  # Se agregó default
    plazo_general = models.TextField(blank=True, null=True, verbose_name="Plazo general")
    requisitos_principales = models.TextField(blank=True, null=True, verbose_name="Requisitos principales")
    url_info = models.URLField(blank=True, null=True, verbose_name="Información oficial")
    impuesto = models.ForeignKey(Impuesto, on_delete=models.PROTECT, related_name='obligaciones', default=1)  # Se mantiene el default

    def __str__(self):
        return self.nombre


class BeneficioCumplimiento(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre del beneficio", db_index=True, default="Beneficio desconocido")  # Se agregó default
    descripcion = models.TextField(verbose_name="Descripción")
    detalle = models.TextField(blank=True, null=True, verbose_name="Detalle adicional")
    url_detalle = models.URLField(blank=True, null=True, verbose_name="Más información")
    impuesto = models.ForeignKey(Impuesto, on_delete=models.PROTECT, related_name='beneficios', default=1)  # Se mantiene el default

    def __str__(self):
        return self.nombre

class PreguntaFrecuente(models.Model):
    pregunta = models.TextField(verbose_name="Pregunta frecuente", db_index=True)
    respuesta = models.TextField(verbose_name="Respuesta")
    url_referencia = models.URLField(blank=True, null=True, verbose_name="Referencia externa")
    impuesto = models.ForeignKey(Impuesto, on_delete=models.PROTECT, related_name='preguntas_frecuentes', default=1)  # Se agregó default=1

    def __str__(self):
        return f"{self.pregunta[:50]}..." if len(self.pregunta) > 50 else self.pregunta

