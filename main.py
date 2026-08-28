from servicios.restaurante import Restaurante

def main():
    app = Restaurante()
    
    while True:
        print("\n--- SISTEMA GESTIÓN RESTAURANTE ---")
        print("1. Listar Productos")
        print("2. Agregar Producto")
        print("3. Registrar Usuario")
        print("4. Realizar Venta")
        print("5. Ver Ventas")
        print("6. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            print("\n--- LISTA DE PRODUCTOS ---")
            for p in app.productos:
                print(f"ID: {p.id_producto} | Nombre: {p.nombre} | Precio: ${p.precio} | Stock: {p.stock}")
        
        elif opcion == "2":
            id_p = input("ID del producto: ")
            nombre = input("Nombre del producto: ")
            precio = float(input("Precio: "))
            stock = int(input("Stock inicial: "))
            app.agregar_producto(id_p, nombre, precio, stock)
            print("Producto agregado correctamente.")
            
        elif opcion == "3":
            id_u = input("ID del usuario: ")
            nombre = input("Nombre del usuario: ")
            tipo = input("Tipo (cliente/empleado): ")
            app.registrar_usuario(id_u, nombre, tipo)
            print("Usuario registrado correctamente.")
            
        elif opcion == "4":
            id_v = input("ID de la venta: ")
            id_u = input("ID del usuario: ")
            id_p = input("ID del producto: ")
            cantidad = int(input("Cantidad a vender: "))
            resultado = app.realizar_venta(id_v, id_u, id_p, cantidad)
            print(resultado)
            
        elif opcion == "5":
            print("\n--- HISTORIAL DE VENTAS ---")
            for v in app.ventas:
                print(f"Venta: {v.id_venta} | Usuario: {v.id_usuario} | Producto: {v.id_producto} | Cantidad: {v.cantidad} | Total: ${v.total}")
                
        elif opcion == "6":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
    