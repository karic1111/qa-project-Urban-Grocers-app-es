## Proyecto de Automatización de Pruebas para Urban Grocers App

## Descripción del Proyecto

Este proyecto lo desarrollé como parte del Sprint N.º 07. Consiste en la automatización
de pruebas para la API de Urban Grocers, específicamente para validar el comportamiento
del endpoint de creación de kits con distintos valores en el campo name.
El objetivo es asegurar que la API responda correctamente frente a entradas válidas e inválidas,
cumpliendo con los criterios establecidos.

## Autor y Sprint

*Karic Pineda Hernández*  
*Sprint N.º 07*

## Tecnologías Utilizadas

Para desarrollar y gestionar este proyecto utilicé las siguientes tecnologías:

- *Python 3.13* – Lenguaje de programación principal  
- *PyTest* – Framework para pruebas automatizadas  
- *Requests* – Librería para realizar peticiones HTTP  
- *PyCharm* – Entorno de desarrollo  
- *Git* – Control de versiones  
- *GitHub* – Repositorio remoto para almacenar y documentar el proyecto

## Configuración del Proyecto

1. Cloné o descargué el repositorio desde GitHub a mi equipo.
2. Me aseguré de tener Python 3.13 instalado.
3. Creé un entorno virtual para el proyecto (opcional pero recomendado):

```bash
python -m venv .venv
.venv\Scripts\activate  # En Windows

4. Instalé las dependencias necesarias usando pip.

Instalación y Uso de Librerías

Para ejecutar correctamente las pruebas, instalé estas librerías:

pip install pytest
pip install requests

También puede usarse un archivo requirements.txt con:

pytest
requests

Y luego instalar todo con:

pip install -r requirements.txt

Cómo ejecutar las pruebas desde la terminal

Para ejecutar las pruebas automatizadas con PyTest, utilicé el siguiente comando:

pytest ruta/del/folder/de/las/pruebas/

Ejemplo si las pruebas están en una carpeta llamada tests:

pytest tests/

O bien, desde la raíz del proyecto simplemente con:

pytest

Esto ejecutará todas las pruebas del proyecto automáticamente.


---

