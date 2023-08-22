# Guía de Uso para el Proyecto CRUD en Python

¡Bienvenido al proyecto CRUD! Esta guía te ayudará a configurar, utilizar y explorar las capacidades del proyecto de manera efectiva. Asegúrate de seguir cada paso cuidadosamente para aprovechar al máximo lo que este proyecto tiene para ofrecer.

## Requisitos Previos

Antes de comenzar, asegúrate de tener lo siguiente instalado en tu sistema:

- Python 3.x
- pip (un sistema de gestión de paquetes para Python)
- virtualenv (una herramienta para crear entornos virtuales)

Si no tienes instalado `virtualenv`, puedes instalarlo utilizando el siguiente comando:

```bash
pip install virtualenv
```

## Pasos para Configurar el Proyecto

Sigue estos pasos para configurar el proyecto en tu entorno local:

### 1. Clonar el Repositorio

```bash
git clone https://github.com/ST3chnical/proyecto-CRUD.git
cd proyecto-CRUD
```

### 2. Crear un Entorno Virtual

Dentro del directorio del proyecto, crea un entorno virtual utilizando `virtualenv` y especificando la versión de Python que deseas usar (en este caso, Python 3):

```bash
virtualenv --python=python3 venv
```

Esto creará un directorio llamado `venv` que contendrá el entorno virtual.

### 3. Activar el Entorno Virtual

Activa el entorno virtual antes de instalar las dependencias y trabajar en el proyecto. Esto aislará las bibliotecas y paquetes específicos del proyecto del sistema global:

En Windows (CMD):
```bash
venv\Scripts\activate
```

En macOS y Linux:
```bash
source venv/bin/activate
```

### 4. Instalar Dependencias

Dentro del entorno virtual activado, instala las dependencias del proyecto utilizando `pip`. Asegúrate de estar ubicado en el directorio principal del proyecto (donde se encuentra el archivo `setup.py`):

```bash
pip install --editable .
```

El flag `--editable` permite que los cambios que realices en el código fuente del proyecto se reflejen inmediatamente sin necesidad de reinstalar.

### 5. Uso del Proyecto

Una vez que hayas configurado el entorno virtual y las dependencias, puedes comenzar a utilizar el proyecto. Para ver una lista de los comandos disponibles y sus descripciones, utiliza el siguiente comando:

```bash
crud --help
```

Este comando te mostrará información sobre cómo usar cada uno de los comandos proporcionados por el proyecto.

### 6. Desactivar el Entorno Virtual

Cuando hayas terminado de trabajar en el proyecto, puedes desactivar el entorno virtual en cualquier momento utilizando el siguiente comando:

```bash
deactivate
```

Esto te llevará de nuevo al entorno de Python global de tu sistema.

¡Listo! Ahora estás listo para usar y contribuir al proyecto CRUD en Python. Siempre recuerda activar el entorno virtual antes de trabajar en el proyecto y desactivarlo cuando hayas terminado. ¡Disfruta codificando y explora los comandos del proyecto con `crud --help`!