class Receta:
    def __init__(self, id_receta, nombre, tiempo, calorias, proteina, dificultad, ingredientes=None):
        self.id = id_receta
        self.nombre = nombre
        self.tiempo = tiempo
        self.calorias = calorias
        self.proteina = proteina
        self.dificultad = dificultad
        self.ingredientes = ingredientes or []

    def __repr__(self):
        return f"Receta({self.nombre} | {self.calorias} kcal | {self.tiempo} min)"