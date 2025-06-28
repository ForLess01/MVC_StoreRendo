class Producto:
    def __init__(self, nombre, categoria, precio):
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio

# Lista para almacenar los productos (simulando una base de datos)
productos = []

def guardar_producto(producto):
    """Guarda un producto en la lista de productos"""
    productos.append(producto)
    return producto

def obtener_productos():
    """Retorna la lista de todos los productos"""
    return productos
