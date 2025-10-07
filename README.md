# 🧪 Proyecto de Automatización de Pruebas para Urban Grocers

## 📖 Descripción del Proyecto  
Este proyecto fue desarrollado como parte del **Sprint N.º 07** del programa **TripleTen LATAM**.  
El objetivo principal fue **automatizar las pruebas de la API de Urban Grocers**, validando el comportamiento del endpoint de **creación de kits** bajo distintos valores en el campo `nombre`.  
Las pruebas garantizan que la API responda correctamente frente a entradas válidas e inválidas, asegurando la estabilidad y el cumplimiento de los criterios funcionales definidos en los requisitos.

---

## 👩‍💻 Autor y Sprint  
**Karic Pineda Hernández**  
**Cohorte 27 - Sprint N.º 07**  
**Plataforma: TripleTen LATAM**

---

## 🧰 Tecnologías utilizadas  
- **Python 3.13** → Lenguaje principal del proyecto.  
- **PyTest** → Framework para la automatización de pruebas.  
- **Requests** → Librería para realizar solicitudes HTTP a la API.  
- **PyCharm** → Entorno de desarrollo.  
- **Git** → Control de versiones.  
- **GitHub** → Repositorio remoto para documentación y almacenamiento del código.

---

## ⚙️ Configuración del Proyecto  
1. Clona o descarga este repositorio desde GitHub:  
   ```bash
   git clone <URL-del-repositorio>
   ```
2. Asegúrate de tener **Python 3.13** instalado en tu equipo.  
3. (Opcional) Crea un entorno virtual para aislar las dependencias:  
   ```bash
   python -m venv .venv
   .venv\Scripts\activate   # En Windows
   source .venv/bin/activate   # En macOS o Linux
   ```
4. Instala las dependencias necesarias:  
   ```bash
   pip install pytest
   pip install requests
   ```

También puedes usar el archivo `requirements.txt` incluido:  
```bash
pip install -r requirements.txt
```

---

## ▶️ Ejecución de Pruebas  
Para ejecutar las pruebas automatizadas con **PyTest**, usa uno de los siguientes comandos:

- Si tus pruebas están dentro de una carpeta llamada `tests`:  
  ```bash
  pytest tests/
  ```

- O bien, desde la raíz del proyecto:  
  ```bash
  pytest
  ```

Esto ejecutará automáticamente todos los casos de prueba definidos en el proyecto.

---

## 🗂 Archivos del Proyecto  
- `tests/` → Carpeta principal donde se encuentran los archivos de prueba automatizados.  
- `main_test.py` → Archivo con los casos de prueba del endpoint de creación de kits.  
- `requirements.txt` → Lista de dependencias necesarias para el proyecto.  
- `README.md` → Este archivo, con toda la documentación del proyecto.

---

## 🧾 Conclusión del Proyecto  
Durante la ejecución de las pruebas, se validaron correctamente los distintos escenarios definidos para el endpoint de **creación de kits**, identificando respuestas correctas ante datos válidos y errores controlados frente a datos inválidos.  
Este proceso permitió asegurar la confiabilidad de la API de Urban Grocers y fortalecer las habilidades en **automatización de pruebas de back-end con PyTest y Requests**. 
