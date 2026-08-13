from servicios.restaurante import Restaurante
from modelos.usuario import Usuario
from modelos.producto import Producto

def menu():
    restaurante = Restaurante()
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Agregar usuario")
        print("2. Agregar producto")
        print("3. Mostrar usuarios")
        print("4. Mostrar productos")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            identificacion = input("Identificación: ")
            nombre = input("Nombre: ")
            correo = input("Correo: ")
            usuario = Usuario(identificacion, nombre, correo)
            restaurante.agregar_usuario(usuario)

        elif opcion == "2":
            codigo = input("Código: ")
            nombre = input("Nombre: ")
            precio = float(input("Precio: "))
            producto = Producto(codigo, nombre, precio)
            restaurante.agregar_producto(producto)

        elif opcion == "3":
            restaurante.mostrar_usuarios()

        elif opcion == "4":
            restaurante.mostrar_productos()

        elif opcion == "5":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción inválida, intente de nuevo.")

if __name__ == "__main__":
    menu()
