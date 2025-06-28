# Sistema de Registro de Productos con MVC

Este es un sistema básico de registro de productos implementado siguiendo el patrón de arquitectura MVC (Modelo-Vista-Controlador) en Python.

## Estructura del Proyecto

```
mvc_tienda/
├── modelo.py         # Clase Producto y funciones de almacenamiento
├── vista.py          # Funciones para mostrar formularios y resultados
├── controlador.py    # Funciones que conectan vista y modelo
└── main.py           # Programa principal con menú interactivo
```

## Requisitos

- Python 3.6 o superior

## Cómo Ejecutar

1. Navega al directorio del proyecto:
   ```
   cd ruta/al/proyecto/mvc_tienda
   ```

2. Ejecuta el programa principal:
   ```
   python main.py
   ```

## Características

- Registro de productos con nombre, categoría y precio
- Listado de productos registrados
- Interfaz de consola intuitiva
- Validación de datos de entrada

## Uso

1. Selecciona la opción "1. Agregar producto" para registrar un nuevo producto
2. Selecciona la opción "2. Listar productos" para ver todos los productos registrados
3. Selecciona la opción "3. Salir" para cerrar la aplicación
