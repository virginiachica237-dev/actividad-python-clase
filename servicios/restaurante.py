from modelos.producto import Producto
from modelos.usuario import Usuario
from modelos.venta import Venta
from servicios.archivo_servicio import ArchivoServicio

class Restaurante:
    def __init__(self):
        self.productos_ruta = "datos/productos.json"
        self.usuarios_ruta = "datos/usuarios.json"
        self.ventas_ruta = "datos/ventas.json"

        self.productos = self.cargar_productos()
        self.usuarios = self.cargar_usuarios()
        self.ventas = self.cargar_ventas()

    def cargar_productos(self):
        data = ArchivoServicio.cargar_datos(self.productos_ruta)
        return [Producto.from_dict(p) for p in data]

    def guardar_productos(self):
        ArchivoServicio.guardar_datos(self.productos_ruta, [p.to_dict() for p in self.productos])

    def cargar_usuarios(self):
        data = ArchivoServicio.cargar_datos(self.usuarios_ruta)
        return [Usuario.from_dict(u) for u in data]

    def guardar_usuarios(self):
        ArchivoServicio.guardar_datos(self.usuarios_ruta, [u.to_dict() for u in self.usuarios])

    def cargar_ventas(self):
        data = ArchivoServicio.cargar_datos(self.ventas_ruta)
        return [Venta.from_dict(v) for v in data]

    def guardar_ventas(self):
        ArchivoServicio.guardar_datos(self.ventas_ruta, [v.to_dict() for v in self.ventas])

    def agregar_producto(self, id_p, nombre, precio, stock):
        producto = Producto(id_p, nombre, precio, stock)
        self.productos.append(producto)
        self.guardar_productos()

    def registrar_usuario(self, id_u, nombre, tipo="cliente"):
        usuario = Usuario(id_u, nombre, tipo)
        self.usuarios.append(usuario)
        self.guardar_usuarios()

    def realizar_venta(self, id_v, id_u, id_p, cantidad):
        producto = next((p for p in self.productos if p.id_producto == id_p), None)
        if not producto:
            return "Error: Producto no encontrado."
        if producto.stock < cantidad:
            return "Error: Stock insuficiente."

        producto.stock -= cantidad
        total = producto.precio * cantidad
        venta = Venta(id_v, id_u, id_p, cantidad, total)
        
        self.ventas.append(venta)
        self.guardar_productos()
        self.guardar_ventas()
        return "Venta realizada con éxito."
        