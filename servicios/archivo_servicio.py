import json
import os

class ArchivoServicio:
    @staticmethod
    def guardar_datos(ruta, datos):
        os.makedirs(os.path.dirname(ruta), exist_ok=True)
        with open(ruta, 'w', encoding='utf-8') as archivo:
            json.dump(datos, archivo, indent=4, ensure_ascii=False)

    @staticmethod
    def cargar_datos(ruta):
        if not os.path.exists(ruta):
            return []
        try:
            with open(ruta, 'r', encoding='utf-8') as archivo:
                return json.load(archivo)
        except json.JSONDecodeError:
            return []
            