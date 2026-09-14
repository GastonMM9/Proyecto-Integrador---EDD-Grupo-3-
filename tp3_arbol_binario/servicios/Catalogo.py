import json
from modelos.arbol_recetas import ArbolBinarioBusqueda
from modelos.receta import Receta

class CatalogoRecetas:
    def __init__(self):
        self.arbol_calorias = ArbolBinarioBusqueda("calorias")
        self.arbol_tiempo = ArbolBinarioBusqueda("tiempo")
        self.arbol_proteina = ArbolBinarioBusqueda("proteina")
        self.lista_recetas = []

    def agregar_receta(self, receta):
        self.lista_recetas.append(receta)
        self.arbol_calorias.insertar(receta)
        self.arbol_tiempo.insertar(receta)
        self.arbol_proteina.insertar(receta)

    def buscar_por_calorias(self, valor):
        return self.arbol_calorias.buscar(valor)

    def listar_todas(self):
        return self.lista_recetas

    def cargar_desde_json(self, ruta):
        try:
            with open(ruta, "r", encoding="utf-8") as f:
                datos = json.load(f)
            for d in datos:
                receta = Receta(
                    d["id"], d["nombre"], d["tiempo"],
                    d["calorias"], d["proteina"], d["dificultad"],
                    d.get("ingredientes", [])
                )
                self.agregar_receta(receta)
            return True
        except FileNotFoundError:
            print(f"No se encontró: {ruta}")
            return False