# ESTRUCTURA --- Ricardo Llerena Delgado ---
----------------------------------------
/scraping_facebook_project
	/fanpages
		fanpages.txt               # Archivo con las URLs de las fanpages

	/src
		__init__.py                # Para marcar la carpeta como un módulo Python
		driver_setup.py            # Script para configurar Selenium y el driver
		scrolling.py               # Script con la lógica de scroll
		extraction.py              # Script que extrae los datos de los posts
		database.py                # Script para manejar la subida a MongoDB
		scraping.py                # Script principal de scraping

	requirements.txt               # Archivo con las dependencias del proyecto
	readme.txt                     # Archivo de instrucciones
	run_scraping.py                # Script principal que ejecuta todo el proceso


----------------------------------------
# Facebook Fanpage Scraper

# Paso 1: Crear un Entorno Virtual en Windows
Un entorno virtual te permite crear un espacio aislado en el que puedes instalar las dependencias del proyecto sin afectar el sistema global.
## 1.1 Dirigirme al directorio donde esta el codigo desde el CMD 
``` Ruta
	cd C:\ruta\de\tu\proyecto
	python -m venv nombre_entorno
	nombre_entorno\Scripts\activate
```
## 1.2 Abrir el Thonny
1. Ve a Herramientas en la barra de menú superior.
2. Selecciona Opciones....
3. En la ventana de opciones, selecciona la pestaña Intérprete.
4. En el menú desplegable, selecciona Usar intérprete local.
```Comando
	C:\ruta\de\tu\proyecto\nombre_entorno\Scripts\python.exe
```

# Paso 2: Instalar Dependencias desde requirements.txt
## 2.1 Crear un archivo requirements.txt:
1. En la carpeta raíz de tu proyecto, crea un archivo llamado requirements.txt. Puedes hacer esto directamente desde Thonny o cualquier editor de texto.
2. Dentro de este archivo, coloca las dependencias necesarias para tu proyecto. Un ejemplo básico podría verse así:
```requirements.txt
	selenium
	pymongo
	webdriver-manager
	python-dotenv
```
## 2.2 Instalar dependencias desde Thonny:
1. Abre el shell de Thonny (la ventana de comandos que aparece en la parte inferior de Thonny).
2. Asegúrate de que el entorno virtual esté activo (en Thonny, esto debería ocurrir automáticamente si lo has configurado antes).
3. Ejecuta el siguiente comando para instalar todas las dependencias desde requirements.txt:

```Codigo para instalar dependencias 
	pip install -r requirements.txt
```
## 2.3 Instalar dependencias desde la terminal de Windows:
1. Si prefieres hacerlo desde la terminal, asegúrate de que el entorno virtual esté activado (ver paso anterior).
```Ejecuta el comando:
	pip install -r requirements.txt
```
Este comando leerá el archivo requirements.txt e instalará todas las librerías necesarias.
```Actualizar el driver
	pip install --upgrade selenium webdriver-manager
```
# Paso 3: Ejecutar el Proyecto desde Thonny
1. Cargar el código principal en Thonny.
2. Asegúrate de que tu entorno virtual esté activado (Thonny lo hará automáticamente si sigues los pasos de creación del entorno virtual dentro de la aplicación).
3. Simplemente presiona el botón de Ejecutar (icono de flecha verde) o utiliza la tecla F5 para ejecutar el código.

# Paso 4: Consideraciones Adicionales
Verificar si las dependencias están instaladas: Puedes verificar si las librerías se han instalado correctamente ejecutando el siguiente comando en Thonny o en la terminal:
```Listado 
	pip list
```
Esto mostrará todas las librerías instaladas en el entorno virtual.

Actualizar dependencias: Si en algún momento necesitas actualizar las dependencias o agregar nuevas, simplemente edita el archivo requirements.txt y vuelve a ejecutar pip install -r requirements.txt.

## Resumen del Flujo
- Crear el entorno virtual (puede ser desde Thonny o la terminal).
- Activar el entorno virtual.
- Crear y/o editar requirements.txt con las dependencias necesarias.
- Instalar dependencias usando pip install -r requirements.txt.
- Ejecutar el código desde Thonny, asegurándote de que el entorno virtual esté activado.
- Este proceso te ayudará a mantener tu entorno de desarrollo ordenado y controlado, especialmente cuando estés usando diferentes
configuraciones en varios proyectos.

