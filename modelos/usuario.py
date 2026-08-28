class Usuario:
    def __init__(self, id_usuario, nombre, tipo="cliente"):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.tipo = tipo

    def to_dict(self):
        return {
            "id_usuario": self.id_usuario,
            "nombre": self.nombre,
            "tipo": self.tipo
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            id_usuario=data["id_usuario"],
            nombre=data["nombre"],
            tipo=data.get("tipo", "cliente")
        )
        