from modelos.arbol_recetas import ArbolBinarioBusqueda
from modelos.ingredientes_y_recetas import Alimento
import json
import os

class CatalogoRecetas:
    def __init__(self):
        self.lista_alimentos = []
        self.arbol_calorias = ArbolBinarioBusqueda("calorias")

    def agregar(self, alimento):
        self.lista_alimentos.append(alimento)
        self.arbol_calorias.insertar(alimento)

    def listar_todos(self):
        return self.arbol_calorias.inorden()

    def listar_ordenados(self):
        return self.arbol_calorias.inorden()

    def listar_preorden(self):
        return self.arbol_calorias.preorden()

    def listar_postorden(self):
        return self.arbol_calorias.postorden()

    def buscar(self, nombre):
        return [r for r in self.arbol_calorias.inorden()
                if nombre.lower() in r.nombre.lower()]

    def cargar_desde_json(self, ruta=None):
        if ruta is None:
            ruta = os.path.join(os.path.dirname(__file__), "..", "datos", "ingredientes_recetas.json")
        
        with open(ruta, encoding="utf-8") as archivo:
            datos = json.load(archivo)
        
        lista = None
        if isinstance(datos, list):
            lista = datos
        else:
            for clave in ["recetas", "alimentos", "datos", "lista"]:
                if clave in datos and isinstance(datos[clave], list):
                    lista = datos[clave]
                    break
        
        if not lista:
            print("⚠️ No se encontró lista de recetas en el JSON")
            return
        
        for dato in lista:
            if isinstance(dato, dict):
                alimento = Alimento(dato)
                self.agregar(alimento)