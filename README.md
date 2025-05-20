# PG2.PRACTICA3

# API de Cultura tributaria

**Descripción**

Esta API proporcionará información clave sobre el sistema tributario, diseñada para promover la cultura tributaria, ya que existe mucha desinformacion respecto al tema. Esto permitirá acceder a información sobre impuestos, obligaciones, conceptos clave (como NIT, RC-IVA, IUE, IVA, IT, etc.), beneficios de cumplir con los tributos y responder preguntas frecuentes......

1.  **Impuestos**
  - `Nombre`
  - `Sigla`
  - `Descripción general`
  - `Sujeto activo`
  - `Sujeto pasivo`
  - `Alícuota`
  - `Conceptos clave relacionados`
  - `Obligaciones relacionadas`

2.  **Obligaciones**
  - `Nombre`
  - `Descripción`
  - `Plazo general`
  - `Requisitos principales`
  - `Impuestos relacionados`

3.  **Conceptos Clave**
  - `Término`
  - `Definición`
  - `Importancia`
  - `Cómo obtenerlo (si aplica)`
    
4.  **Beneficios del Cumplimiento**
  - `Descripción`
  - `Detalle`
    
5.  **Preguntas Frecuentes**
  - `Pregunta`
  - `Respuesta`

El objetivo de esta API es facilitar el desarrollo de aplicaciones educativas e integrar contenido tributario en plataformas escolares, universitarias o gubernamentales de Bolivia, contribuyendo a una mejor comprensión y cumplimiento fiscal en el país.

## Requisitos previos
- Python 3.12 instalado
- pip

## Crear entorno virtual
1. Abrir la terminal en el directorio del proyecto
2. Ejecutar el siguiente comando a continuación:

```bash
python -m venv env
```
Esto permitirá crear un directorio llamado `env` en el entorno virtual.

## Activar entorno virtual

* **Windows:**
```bash
.\env\Scripts\activate
```

* **Linux/Mac:**
```bash
source env/bin/activate
```
Después de activar el entorno virtual, `(env)` se mostrará al inicio de la linea de comandos.

## Crear archivo
Crear el archivo `requirements.txt` y dentro agregar:

```bash
django==5.2
django-extensions==4.1
djangorestframework==3.16.0
```
## Instalar dependencias
Tras la creacion del archivo usa `pip` para instalar las dependencias del proyecto:

```bash
pip install -r requirements.txt
```
## Desactivar entorno virtual
Cuando hayas terminado de trabajar en el proyecto, puedes desactivar el entorno virtual para volver a tu entorno global con este simple comando.

```bash
deactivate
```
## Crear proyecto Django
Para iniciar un nuevo proyecto, ejecuta:

```bash
django-admin startproject apitributaria .
```

## Aplicar migraciones
Aplica los cambios definidos a la base de datos mediante:

```bash
python manage.py migrate
```

## Iniciar servidor
Inicia el servidor de desarrollo para ver tu aplicación en funcionamiento con:

```bash
python manage.py runserver
```

## Crear superusuario
Crea un usuario con privilegios de administrador para gestionar su sitio `Django`

```bash
python manage.py createsuperuser
```

## Crear aplicación
Utiliza este comando para generar la estructura de archivos de la nueva aplicación. 

```bash
python manage.py startapp servicios
```

## Agregar aplicación a settings.py
    'django_extensions',
En este punto es enecesario agregar el nombre de `django_extensions`y `servicios` a la lista `INSTALLED_APPS` dentro del archivo `settings.py` del proyecto, lo que informa a Django que esta aplicación debe ser tenida en cuenta.

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'servicios',
]
```
## Crear modelo

Escribe el modelo en `librosservicios/models.py`:

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

## Migrar la base de datos

```powershell
python manage.py makemigrations

```
```
python manage.py migrate

```

## Diagramar el MER de `models.py` usando Graphviz

Instalalo en tu sistema, puedes descargarlo desde: https://graphviz.gitlab.io/download/

luego ejecuta:

```bash
python manage.py graph_models servicios -o modelo.png
```
Este comando generara una imagen con nombre de `modelo.py` directamnente en la carpeta de `servicios`con el diagrama entidad y relacion

## Visualizacion del diagrama

Abre el archivo `modelo.png` y veras el diagrama MER.

