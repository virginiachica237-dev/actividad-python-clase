##Restaurante App
 Descripción
Aplicación en Python que simula la gestión de un restaurante.  
Permite agregar productos al menú, registrar clientes y asignar pedidos.  
Se utiliza programación orientada a objetos, constructores, decoradores y una clase de servicio.
## Estructura del proyecto
restaurante_app/
├── modelos/
│   ├── init.py
│   ├── producto.py
│   └── cliente.py
├── servicios/
│   ├── init.py
│   └── restaurante.py
└── main.py
##Características
- Uso de **constructores** en las clases `Producto` y `Cliente`.
- Aplicación de **decoradores** (`@property`, `@setter`) para manejar atributos.
- Creación dinámica de objetos mediante un **menú interactivo**.
- Clase de servicio `Restaurante` que gestiona menú y clientes.
- Ejecución principal desde `main.py`.
 Ejecución
Para correr la aplicación:
```bash
python main.py
Menú del restaurante:
Pizza - $8.5
Hamburguesa - $5.0
Ensalada - $4.0
Clientes registrados:
Cliente: Elvira, Pedidos: ['Pizza', 'Ensalada']
Cliente: Carlos, Pedidos: ['Hamburguesa ']
def main():
    restaurante = Restaurante()
    while True:
        print("\n--- Menú Principal ---")
        print("1. Agregar producto")
        print("2. Registrar cliente")
        print("3. Mostrar menú")
        print("4. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            nombre = input("Nombre del producto: ")
            precio = float(input("Precio: "))
            restaurante.agregar_producto(nombre, precio)
        elif opcion == "2":
            nombre = input("Nombre del cliente: ")
            restaurante.registrar_cliente(nombre)
        elif opcion == "3":
            restaurante.mostrar_menu()
        elif opcion == "4":
            break
        else:
            print("Opción inválida")

## Autor
Elvira [Chica]


