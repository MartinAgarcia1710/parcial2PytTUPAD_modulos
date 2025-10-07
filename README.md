# 📚 Sistema de Gestión de Biblioteca Escolar

Este proyecto es una versión modularizada del sistema de gestión de biblioteca escolar desarrollado en Python por **Alberto Cortez**.
El objetivo principal fue **reestructurar el código original** para mejorar su **organización, mantenimiento y reutilización**, aplicando una **arquitectura por paquetes y módulos** sin alterar su funcionalidad original.

---

## 🧩 Estructura del Proyecto

El proyecto se organizó bajo una estructura de paquetes con responsabilidades bien definidas:

```markdown
biblioteca/
│
├── datos/
│   ├── __init__.py
│   ├── persistencia.py
│   └── catalogo.csv
│
├── operaciones/
│   ├── __init__.py
│   ├── ingreso.py
│   ├── consulta.py
│   ├── gestion.py
│   └── agotados.py
│
├── ui/
│   ├── __init__.py
│   └── menu.py
│
└── main.py
```

### 📁 `datos/`

Contiene los módulos encargados del manejo de archivos y persistencia de datos.

* **persistencia.py**: carga y guarda la información del catálogo desde y hacia un archivo CSV.
* **catalogo.csv**: archivo donde se almacenan los datos de títulos y ejemplares.

### ⚙️ `operaciones/`

Incluye los módulos funcionales del sistema, organizados según su propósito:

* **ingreso.py**: manejo del ingreso de títulos y ejemplares.
* **consulta.py**: búsqueda y visualización del catálogo.
* **gestion.py**: préstamo, devolución y actualización de ejemplares.
* **agotados.py**: listado de títulos sin ejemplares disponibles.

### 🖥️ `ui/`

Responsable de la interacción con el usuario:

* **menu.py**: muestra el menú principal y gestiona la selección de opciones.

### 🧠 `main.py`

Punto de entrada del programa. Coordina la ejecución general del sistema llamando a los módulos correspondientes.

---

## 🚀 Ejecución del Programa

1. Clonar o descargar el repositorio.
2. Asegurarse de tener **Python 3.10+** instalado.
3. Ejecutar el programa desde la terminal o desde Visual Studio Code con:

```bash
python main.py
```

---

## 🧠 Objetivos de la Modularización

* Eliminar el uso de variables globales.
* Favorecer la **separación de responsabilidades** (principio de modularidad).
* Facilitar el **mantenimiento y la extensión del código**.
* Mantener la **misma funcionalidad** y lógica original.

---

## 👨‍🏫 Créditos

Proyecto basado en el código original del profesor **Alberto Cortez**, adaptado con fines académicos para la enseñanza de **estructuras de control, manejo de listas y modularización en Python**.

Modularización y documentación por: **[Martín Alejandro García]**

