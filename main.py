from servicios.restaurante import Restaurante
from modelos.producto import Producto
from modelos.bebida import Bebida
from modelos.cliente import Cliente

def mostrar_menu():
    print("\n--- Menú Restaurante Cobijo ---")
    print("1. Registrar producto Pollo ($12)")
    print("2. Registrar bebida Jugo ($3)")
    print("3. Registrar cliente Elvira")
    print("4. Registrar producto Papas ($5)")
    print("5. Mostrar productos")
    print("6. Mostrar clientes")
    print("7. Salir")

def main():
    restaurante = Restaurante("Cobijo")

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            producto = Producto("Pollo", 12.0, "Comida")
            restaurante.agregar_producto(producto)
            print("Producto Pollo ($12) registrado correctamente.")

        elif opcion == "2":
            bebida = Bebida("Jugo", 3.0, "Mediano")
            restaurante.agregar_producto(bebida)
            print("Bebida Jugo ($3) registrada correctamente.")

        elif opcion == "3":
            cliente = Cliente("Elvira")
            restaurante.agregar_cliente(cliente)
            print("Cliente Elvira registrado correctamente.")

        elif opcion == "4":
            producto = Producto("Papas", 5.0, "Comida")
            restaurante.agregar_producto(producto)
            print("Producto Papas ($5) registrado correctamente.")

        elif opcion == "5":
            restaurante.mostrar_productos()

        elif opcion == "6":
            restaurante.mostrar_clientes()

        elif opcion == "7":
            print("¡Gracias por usar el sistema Cobijo!")
            break

        else:
            print("Opción inválida, intente de nuevo.")

if __name__ == "__main__":
    main()
