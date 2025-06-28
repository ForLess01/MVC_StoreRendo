from modelo import Producto, guardar_producto, obtener_productos

def agregar_producto():
    """Controla el flujo para agregar un nuevo producto"""
    from vista import mostrar_formulario_producto
    
    # Obtener datos del producto desde la vista
    datos_producto = mostrar_formulario_producto()
    
    # Crear instancia de Producto
    nuevo_producto = Producto(
        nombre=datos_producto['nombre'],
        categoria=datos_producto['categoria'],
        precio=datos_producto['precio']
    )
    
    # Guardar el producto
    producto_guardado = guardar_producto(nuevo_producto)
    print(f"\n¡Producto '{producto_guardado.nombre}' guardado exitosamente!")

def listar_productos():
    """Controla el flujo para listar todos los productos"""
    from vista import mostrar_productos
    
    # Obtener productos del modelo
    productos = obtener_productos()
    
    # Mostrar productos usando la vista
    mostrar_productos(productos)
