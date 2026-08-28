class Venta:
    def __init__(self, id_venta, id_usuario, id_producto, cantidad, total):
        self.id_venta = id_venta
        self.id_usuario = id_usuario
        self.id_producto = id_producto
        self.cantidad = int(cantidad)
        self.total = float(total)

    def to_dict(self):
        return {
            "id_venta": self.id_venta,
            "id_usuario": self.id_usuario,
            "id_producto": self.id_producto,
            "cantidad": self.cantidad,
            "total": self.total
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            id_venta=data["id_venta"],
            id_usuario=data["id_usuario"],
            id_producto=data["id_producto"],
            cantidad=data["cantidad"],
            total=data["total"]
        )
