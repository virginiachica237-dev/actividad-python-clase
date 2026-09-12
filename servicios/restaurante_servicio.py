from modelos.producto import Producto
from modelos.usuario import Usuario
from servicios.archivo_servicio import ArchivoServicio

class RestauranteServicio:
    def __init__(self):
        self.ruta_usuarios = "datos/usuarios.json"
        self.ruta_productos = "datos/productos.json"

    def obtener_usuarios(self):
        datos = ArchivoServicio.leer_json(self.ruta_usuarios)
        return [Usuario(u["usuario"], u["password"]) for u in datos]

    def obtener_productos(self):
        datos = ArchivoServicio.leer_json(self.ruta_productos)
        return [Producto(p["nombre"], p["precio"], p["stock"]) for p in datos]

    def validar_login(self, username, password):
        usuarios = self.obtener_usuarios()
        for u in usuarios:
            if u.usuario == username and u.password == password:
                return True
        return False