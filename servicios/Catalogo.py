from estructura.arbol_binario import ArbolBinarioBusqueda
from modelos.receta import Receta
from modelos.arbol_avl_receta import ArbolAVLRecetas
from estructuras.arbol_general import ArbolGeneral  


class CatalogoRecetas:
    def __init__(self):
        self.lista_recetas = []
        self.arbol_calorias = ArbolBinarioBusqueda()
        self.arbol_nombre = ArbolBinarioBusqueda()  
        
        # Árbol AVL — equilibrado
        self.arbol_avl_nombre = ArbolAVLRecetas("nombre")
        self.arbol_avl_calorias = ArbolAVLRecetas("calorias")
        
        # === TP5 — ÁRBOL GENERAL === 
        self.arbol_categorias = ArbolGeneral()
        self._crear_categorias()

    def _crear_categorias(self):
        """Crea la jerarquía: Categorías → Subcategorías"""
        raiz = self.arbol_categorias.insertar_raiz("Categorías de Recetas")
        self.saludable = self.arbol_categorias.agregar_hijo(raiz, "Saludable")
        self.rapida = self.arbol_categorias.agregar_hijo(raiz, "Rápida")
        self.tradicional = self.arbol_categorias.agregar_hijo(raiz, "Tradicional")

    def _agregar_a_categoria(self, receta):
        """Agrega la receta a su categoría en el árbol general"""
        cat = getattr(receta, 'categoria', 'Tradicional').lower()
        nodo_padre = getattr(self, cat, self.tradicional)
        self.arbol_categorias.agregar_hijo(nodo_padre, receta)

    def agregar_receta(self, receta):
        self.lista_recetas.append(receta)
        self.arbol_calorias.insertar(receta.calorias)
        self.arbol_nombre.insertar(receta)
        self.arbol_avl_nombre.insertar(receta)
        self.arbol_avl_calorias.insertar(receta)
        self._agregar_a_categoria(receta) 

    def listar_todas(self):
        return self.lista_recetas

    def listar_ordenadas_por_calorias(self):
        return self.arbol_calorias.inorden()

    def buscar_por_calorias(self, minimo, maximo):
        return self.arbol_calorias.buscar_por_rango(minimo, maximo)

    def buscar_por_calorias_arbol(self, valor):
        return self.arbol_calorias.buscar(valor)

    def listar_inorden(self):
        return self.arbol_calorias.inorden()

    def listar_preorden(self):
        return self.arbol_calorias.preorden()

    def listar_postorden(self):
        return self.arbol_calorias.postorden()

    # ===== MÉTODOS TP5 — ÁRBOL GENERAL ===== 
    def explorar_amplitud(self):
        return self.arbol_categorias.amplitud()
    
    def explorar_profundidad(self):
        return self.arbol_categorias.profundidad_preorder()

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
                ingredientes=d.get('ingredientes', []),
                categoria=d.get('categoria', 'Tradicional')  
            )
            self.agregar_receta(receta)
