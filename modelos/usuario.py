class Usuario:
    def __init__(self, username, rol, activo=True):
        self.username = username
        self.rol = rol
        self.activo = activo

    def to_dict(self):
        return {
            "username": self.username,
            "rol": self.rol,
            "activo": self.activo
        }

    @classmethod
    def from_dict(cls, datos):
        return cls(
            username=datos.get("username"),
            rol=datos.get("rol"),
            activo=datos.get("activo", True)
        )
