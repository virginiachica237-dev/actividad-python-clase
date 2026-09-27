from ventas import Venta, listar_ventas

while True:
    print("1. Registrar venta")
    print("2. Listar ventas")
    print("3. Salir")
    opcion = input("Elige una opción: ")

    if opcion == "1":
        cliente = input("Nombre del cliente: ")
        producto = input("Producto: ")
        cantidad = int(input("Cantidad: "))
        venta = Venta(cliente, producto, cantidad)
        venta.guardar()
        print("Venta registrada correctamente.")
    elif opcion == "2":
        listar_ventas()
    elif opcion == "3":
        break
    else:
        print("Opción no válida.")
