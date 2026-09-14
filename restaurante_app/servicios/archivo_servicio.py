import json

class ArchivoServicio:
    @staticmethod
    def leer_json(ruta):
        with open(ruta, "r", encoding="utf-8") as f:
            return json.load(f)
