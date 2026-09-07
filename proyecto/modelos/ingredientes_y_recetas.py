class Alimento:
    def __init__(self, nombre, categoria, vencimiento, cantidad):
        self._nombre = nombre
        self._categoria = categoria
        self._vencimiento = vencimiento
        self._cantidad = cantidad
    
    @property
    def nombre(self):
        return self._nombre
    
    @property
    def categoria(self):
        return self._categoria
    
    @property
    def vencimiento(self):
        return self._vencimiento
    
    @property
    def cantidad(self):
        return self._cantidad
    
    def __repr__(self):
        return f"{self._nombre} ({self._categoria}) 🗓️{self._vencimiento} 📦{self._cantidad}"


class Receta:
    def __init__(self, nombre, ingredientes, tiempo, objetivo, dificultad):
        self._nombre = nombre
        self._ingredientes = ingredientes
        self._tiempo = tiempo
        self._objetivo = objetivo
        self._dificultad = dificultad
    
    @property
    def nombre(self):
        return self._nombre
    
    @property
    def ingredientes(self):
        return self._ingredientes
    
    @property
    def tiempo(self):
        return self._tiempo
    
    @property
    def objetivo(self):
        return self._objetivo
    
    @property
    def dificultad(self):
        return self._dificultad
    
    def __repr__(self):
        return f"{self._nombre} - {self._objetivo} ({self._dificultad}) ⏱️{self._tiempo}min 🍽️{len(self._ingredientes)} ingredientes"