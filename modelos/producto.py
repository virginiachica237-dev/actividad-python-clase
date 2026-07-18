class Producto:
    def __init__(self, nombre, precio, tipo):
        self.nombre = nombre
        self.precio = precio
        self.tipo = tipo

    def __str__(self):
        return f"{self.tipo}: {self.nombre} - ${self.precio:.2f}"
