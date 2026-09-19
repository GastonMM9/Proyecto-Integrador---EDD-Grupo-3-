class Alimento:
    def __init__(self, datos=None):
        if isinstance(datos, dict):
            self.nombre = datos.get("nombre", "")
            self.calorias = datos.get("calorias", 0)
            self.proteina = datos.get("proteina", 0)
            self.tiempo = datos.get("tiempo_minutos", 0)
            self.dificultad = datos.get("dificultad", "")
            self.ingredientes = datos.get("ingredientes", [])
        else:
            self.nombre = ""
            self.calorias = 0
            self.proteina = 0
            self.tiempo = 0
            self.dificultad = ""
            self.ingredientes = []

    def __str__(self):
        return f"{self.nombre} | {self.calorias} kcal | {self.proteina}g proteína"
