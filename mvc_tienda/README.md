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

## Preguntas de Reflexión

1. **¿Qué ventajas identificas al usar MVC en sistemas de información?**
   - Separación clara de responsabilidades
   - Código más mantenible y escalable
   - Facilita el trabajo en equipo al dividir el desarrollo en capas
   - Permite modificar una capa sin afectar a las demás

2. **¿Qué pasaría si no separamos la lógica en Modelo, Vista y Controlador?**
   - El código sería más difícil de mantener y entender
   - Mayor propensión a errores al modificar el código
   - Dificultad para hacer cambios en la interfaz sin afectar la lógica de negocio
   - Pruebas más complejas y menos efectivas

3. **¿Cómo aplicarías este patrón en un sistema más complejo (como uno de matrículas)?**
   - **Modelo:** Clases como Estudiante, Curso, Matricula con sus respectivas relaciones
   - **Vista:** Interfaces para registro de estudiantes, oferta de cursos, proceso de matrícula
   - **Controlador:** Gestionaría las interacciones entre modelos y vistas, validando reglas de negocio
   - Se podrían añadir más capas como servicios y repositorios para mayor escalabilidad
