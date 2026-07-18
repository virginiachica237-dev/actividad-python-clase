class Restaurante:
    def __init__(self, nombre):
        self.nombre = nombre
        self.productos = []
        self.clientes = []

    def agregar_producto(self, producto):
        self.productos.append(producto)
        print(f"Producto agregado: {producto}")

    def mostrar_productos(self):
        if not self.productos:
            print("No hay productos registrados.")
        else:
            print("\n--- Productos ---")
            for p in self.productos:
                print(p)

    def agregar_cliente(self, cliente):
        self.clientes.append(cliente)
        print(f"Cliente agregado: {cliente}")

    def mostrar_clientes(self):
        if not self.clientes:
            print("No hay clientes registrados.")
        else:
            print("\n--- Clientes ---")
            for c in self.clientes:
                print(c)
