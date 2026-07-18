from modelos.producto import Producto

class Bebida(Producto):
    def __init__(self, nombre, precio, tamaño):
        super().__init__(nombre, precio, "Bebida")
        self.tamaño = tamaño

    def __str__(self):
        return f"{self.tipo}: {self.nombre} ({self.tamaño}) - ${self.precio:.2f}"
