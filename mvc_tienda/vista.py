def mostrar_menu():
    """Muestra el menú principal y retorna la opción seleccionada"""
    print("\n=== SISTEMA DE REGISTRO DE PRODUCTOS - StoreRendo ===")
    print("1. Agregar producto")
    print("2. Listar productos")
    print("3. Salir")
    
    while True:
        try:
            opcion = int(input("\nSeleccione una opción: "))
            if 1 <= opcion <= 3:
                return opcion
            else:
                print("Por favor, seleccione una opción válida (1-3)")
        except ValueError:
            print("Por favor, ingrese un número válido")

def mostrar_formulario_producto():
    """Solicita los datos de un producto y los retorna como un diccionario"""
    print("\n--- NUEVO PRODUCTO ---")
    nombre = input("Nombre del producto: ")
    categoria = input("Categoría: ")
    
    while True:
        try:
            precio = float(input("Precio: "))
            if precio > 0:
                break
            else:
                print("El precio debe ser mayor a 0")
        except ValueError:
            print("Por favor, ingrese un precio válido")
    
    return {"nombre": nombre, "categoria": categoria, "precio": precio}

def mostrar_productos(lista_productos):
    """Muestra la lista de productos en formato de tabla"""
    if not lista_productos:
        print("\nNo hay productos registrados.")
        return
    
    print("\n--- LISTA DE PRODUCTOS ---")
    print(f"{'ID':<5} {'NOMBRE':<20} {'CATEGORÍA':<15} {'PRECIO':>10}")
    print("-" * 55)
    
    for i, producto in enumerate(lista_productos, 1):
        print(f"{i:<5} {producto.nombre:<20} {producto.categoria:<15} S/.{producto.precio:>8.2f}")
    
    print("-" * 55)
    print(f"Total de productos: {len(lista_productos)}")
