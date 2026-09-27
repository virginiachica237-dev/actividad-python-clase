import json

class Venta:
    def __init__(self, cliente, producto, cantidad):
        self.cliente = cliente
        self.producto = producto
        self.cantidad = cantidad

    def guardar(self):
        venta = {
            "cliente": self.cliente,
            "producto": self.producto,
            "cantidad": self.cantidad
        }
        try:
            with open("ventas.json", "r") as f:
                datos = json.load(f)
        except FileNotFoundError:
            datos = []

        datos.append(venta)

        with open("ventas.json", "w") as f:
            json.dump(datos, f, indent=4)

# Nueva función para listar ventas
def listar_ventas():
    try:
        with open("ventas.json", "r") as f:
            datos = json.load(f)
            for v in datos:
                print(f"Cliente: {v['cliente']}, Producto: {v['producto']}, Cantidad: {v['cantidad']}")
    except FileNotFoundError:
        print("No hay ventas registradas todavía.")
