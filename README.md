# PG2.PRACTICA3

# API de Cultura tributaria

**Descripción**

Esta API proporcionará información clave sobre el sistema tributario boliviano, diseñada para promover la cultura tributaria y combatir la desinformación respecto al tema. La API permitirá acceder a información sobre impuestos, obligaciones, conceptos clave (como NIT, RC-IVA, IUE, IVA, IT, etc.), beneficios de cumplir con los tributos y respuestas a preguntas frecuentes.

El objetivo de esta API es facilitar el desarrollo de aplicaciones educativas e integrar contenido tributario en plataformas escolares, universitarias o gubernamentales de Bolivia, contribuyendo a una mejor comprensión y cumplimiento fiscal en el país.

La API ha sido implementada utilizando Django y Django REST Framework, enfocándose en la exposición de datos de solo lectura para garantizar la seguridad, por lo que no requiere autenticación para su consumo.

## DIAGRAMA DE MODELOS
## Diagramar el MER de models.py usando Graphviz

Instalalo en tu sistema, puedes descargarlo desde: https://graphviz.gitlab.io/download/

luego ejecuta:

bash
python manage.py graph_models servicios -o modelo.png

Este comando generara una imagen con nombre de modelo.py directamnente en la carpeta de `servicios`con el diagrama entidad y relacion

## Visualizacion del diagrama

Abre el archivo modelo.png y veras el diagrama MER.
![Diagrama de modelos](modelo.png)

-----------------------------------------------------

## ENDPOINTS DISPONIBLES Y SUS EJEMPLOS DE RESPUESTAS APLICADAS.

1.Una plataforma web o app móvil educativa puede usar esta API para mostrar a estudiantes información clara sobre los tipos de impuestos por ejemplo (IVA, IT, RC-IVA,IUE, etc), conceptos clave como NIT, credito fiscval, debito fiscal,etc

Con el OBJETIVO de enseñar desde edades tempranas el rol y funcionamiento de los tributos.

Usando el endpoint GET/api/impuestos/
Usando el endpoint GET/api/conceptos_clave/


2.Chatbot Tributario o Asistente Virtual, donde desarrolladores pueden integrar esta API en un bot que responda preguntas frecuentes de forma automatizada, por ejemplo vía WhatsApp o web.

Con el OBJETIVO de ofrecer asistencia basica 24/7 sobre temas tributarios. 

Usando el endpoint GET/api/preguntas_frecuentes/


### **`/api/impuestos/`** 
**Método:** `GET`
**Descripción:** Lista todos los impuestos registrados.

```json
{
    "id": 1,
    "nombre": "Impuesto al Valor Agregado (IVA)",
    "descripcion": "Impuesto indirecto sobre el consumo de bienes y servicios.",
    "plazo_general": "Aplica en la compra de bienes y servicios profesionales.",
    "sujeto_activo": "Estado",
    "sujeto_pasivo": "Contribuyente",
    "alicuota": 13
}


### `/api/obligaciones/`  
**Método:** `GET`
**Descripción:** Lista todas las obligaciones fiscales.

{
    "id": 2,
    "nombre": "Declaración Mensual IVA",
    "descripcion": "Presentación mensual del formulario IVA.",
    "plazo_general": "Hasta el día 20 del mes siguiente.",
    "requisitos_principales": "Registro de compras y ventas.",
    "impuestos_relacionados": ["IVA"]
}


### `/api/conceptos_clave/`  
**Método:** `GET` 
**Descripción:** Lista todos los conceptos clave tributarios.

{
    "id": 3,
    "termino": "Crédito Fiscal",
    "definicion": "Monto de IVA pagado que puede usarse para descontar del IVA por pagar.",
    "importancia": "Permite evitar doble tributación.",
    "como_obtenerlo": "Presentando comprobantes válidos de compras."
}


### `/api/beneficios/`
**Método:** `GET`
**Descripción:** Lista los beneficios tributarios por cumplimiento.

[
    {
        "id": 4,
        "nombre": "Descuento por pronto pago",
        "descripcion": "Si se paga antes del vencimiento, se recibe un 5% de descuento."
    },
    {
        "id": 4.1,
        "nombre": "Acceso a líneas de crédito",
        "descripcion": "Los contribuyentes cumplidos pueden aplicar a programas financieros del Estado."
    }
]


### `/api/preguntas_frecuentes/`
**Método:** `GET`
**Descripción:** Lista las preguntas frecuentes sobre cultura tributaria.

[
    {
        "id": 5,
        "pregunta": "¿Qué es el NIT?",
        "respuesta": "El Número de Identificación Tributaria es un código único para cada contribuyente."
    },
    {
        "id": 5.1,
        "pregunta": "¿Cuándo debo declarar IVA?",
        "respuesta": "Antes del día 20 del mes siguiente al periodo declarado."
    }
]




