from estructura.arbol_binario import ArbolBinarioBusqueda
from modelos.receta import Receta
from modelos.arbol_avl_receta import ArbolAVLRecetas
class CatalogoRecetas:
    def __init__(self):
        self.lista_recetas = []
        self.arbol_calorias = ArbolBinarioBusqueda()
        # Árbol AVL — equilibrado
        self.arbol_avl_nombre = ArbolAVLRecetas("nombre")
        self.arbol_avl_calorias = ArbolAVLRecetas("calorias")
    def agregar_receta(self, receta):
        self.lista_recetas.append(receta)
        self.arbol_calorias.insertar(receta.calorias)
        self.arbol_nombre.insertar(receta)
        self.arbol_avl_nombre.insertar(receta)
        self.arbol_avl_calorias.insertar(receta)
    def listar_todas(self):
        return self.lista_recetas

    def listar_ordenadas_por_calorias(self):
        return self.arbol_calorias.inorden()

    def buscar_por_calorias(self, minimo, maximo):
        return self.arbol_calorias.buscar_por_rango(minimo, maximo)

    def cargar_desde_json(self, ruta):
        import json
        with open(ruta, encoding='utf-8') as f:
            datos = json.load(f)
        for d in datos:
            receta = Receta(
                nombre=d['nombre'],
                tiempo=d['tiempo_minutos'],
                calorias=d['calorias'],
                proteina=d.get('proteina', 0),
                dificultad=d.get('dificultad', 'Media'),
                ingredientes=d.get('ingredientes', [])
            )
            self.agregar_receta(receta)
            
def buscar_por_calorias_arbol(self, valor):
        return self.arbol_calorias.buscar(valor)

    def listar_inorden(self):
        return self.arbol_calorias.inorden()

    def listar_preorden(self):
        return self.arbol_calorias.preorden()

    def listar_postorden(self):
        return self.arbol_calorias.postorden()

    def cargar_desde_json(self, ruta):
        import json
        with open(ruta, encoding='utf-8') as f:
            datos = json.load(f)
        for d in datos:
            receta = Receta(
                nombre=d['nombre'],
                tiempo=d['tiempo_minutos'],
                calorias=d['calorias'],
                proteina=d.get('proteina', 0),
                dificultad=d.get('dificultad', 'Media'),
                ingredientes=d.get('ingredientes', [])
            )
            self.agregar_receta(receta)
+
