from controlador import agregar_producto, listar_productos
from vista import mostrar_menu

def main():
    while True:
        opcion = mostrar_menu()
        
        if opcion == 1:
            agregar_producto()
        elif opcion == 2:
            listar_productos()
        elif opcion == 3:
            print("\n¡Gracias por usar el Sistema de Registro de Productos - StoreRendo!")
            break

if __name__ == "__main__":
    main()
