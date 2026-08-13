from modelos.usuario import Usuario
from modelos.producto import Producto

class Restaurante:
    def __init__(self):
        self.usuarios = []
        self.productos = []

    def agregar_usuario(self, usuario: Usuario):
        self.usuarios.append(usuario)

    def agregar_producto(self, producto: Producto):
        self.productos.append(producto)

    def mostrar_usuarios(self):
        if not self.usuarios:
            print("No hay usuarios registrados.")
        else:
            for u in self.usuarios:
                print(u)

    def mostrar_productos(self):
        if not self.productos:
            print("No hay productos registrados.")
        else:
            for p in self.productos:
                print(p)
