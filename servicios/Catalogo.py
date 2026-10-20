from estructura.arbol_binario import ArbolBinarioBusqueda
from modelos.receta import Receta
from modelos.arbol_avl_receta import ArbolAVLRecetas
from estructuras.arbol_general import ArbolGeneral

# ==============================================
# TP6: COLA DE PRIORIDAD — HEAP BINARIO
# ==============================================
def calcular_prioridad(receta):
    peso_calorias = 0.4
    peso_proteina = 0.4
    peso_tiempo = 0.2

    calorias_inv = 1 / (receta.calorias + 1)
    tiempo_inv = 1 / (receta.tiempo_minutos + 1)

    return (peso_calorias * calorias_inv +
            peso_proteina * (receta.proteina / 100) +
            peso_tiempo * tiempo_inv)


class ColaPrioridadHeap:
    def __init__(self):
        self.heap = []

    def _indice_padre(self, i):
        return (i - 1) // 2

    def _indice_hijo_izq(self, i):
        return 2 * i + 1

    def _indice_hijo_der(self, i):
        return 2 * i + 2

    def _intercambiar(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def _flotar(self, i):
        while i > 0:
            padre = self._indice_padre(i)
            if calcular_prioridad(self.heap[i]) > calcular_prioridad(self.heap[padre]):
                self._intercambiar(i, padre)
                i = padre
            else:
                break

    def _hundir(self, i):
        n = len(self.heap)
        while True:
            izq = self._indice_hijo_izq(i)
            der = self._indice_hijo_der(i)
            mayor = i
            if izq < n and calcular_prioridad(self.heap[izq]) > calcular_prioridad(self.heap[mayor]):
                mayor = izq
            if der < n and calcular_prioridad(self.heap[der]) > calcular_prioridad(self.heap[mayor]):
                mayor = der
            if mayor != i:
                self._intercambiar(i, mayor)
                i = mayor
            else:
                break

    def insertar(self, elemento):
        self.heap.append(elemento)
        self._flotar(len(self.heap) - 1)

    def extraer_maximo(self):
        if not self.heap:
            return None
        maximo = self.heap[0]
        ultimo = self.heap.pop()
        if self.heap:
            self.heap[0] = ultimo
            self._hundir(0)
        return maximo

    def obtener_top_n(self, n):
        copia = self.heap.copy()
        resultado = []
        for _ in range(min(n, len(self.heap))):
            resultado.append(self.extraer_maximo())
        self.heap = copia
        return resultado


class CatalogoRecetas:
    def __init__(self):
        self.lista_recetas = []
        self.arbol_calorias = ArbolBinarioBusqueda()
        self.arbol_nombre = ArbolBinarioBusqueda()
        self.arbol_avl_nombre = ArbolAVLRecetas("nombre")
        self.arbol_avl_calorias = ArbolAVLRecetas("calorias")
        self.arbol_categorias = ArbolGeneral()
        self._crear_categorias()

        # === TP6: Cola de prioridad ===
        self.cola_prioridad = ColaPrioridadHeap()

    def _crear_categorias(self):
        raiz = self.arbol_categorias.insertar_raiz("Categorías de Recetas")
        self.saludable = self.arbol_categorias.agregar_hijo(raiz, "Saludable")
        self.rapida = self.arbol_categorias.agregar_hijo(raiz, "Rápida")
        self.tradicional = self.arbol_categorias.agregar_hijo(raiz, "Tradicional")

    def _agregar_a_categoria(self, receta):
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

        # TP6: Agregar a la cola
        self.cola_prioridad.insertar(receta)

    def listar_todas(self):
        return self.lista_recetas

    def listar_ordenadas_por_calorias(self):
        return sorted(self.lista_recetas, key=lambda r: r.calorias)

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

    # TP5
    def explorar_amplitud(self):
        return self.arbol_categorias.amplitud()

    def explorar_profundidad(self):
        return self.arbol_categorias.profundidad_preorder()

    # TP6: Obtener Top-N
    def obtener_top_recomendaciones(self, n=5):
        top = self.cola_prioridad.obtener_top_n(n)
        print(f"\n=== TOP {n} RECOMENDACIONES ===")
        for idx, receta in enumerate(top, 1):
            prioridad = calcular_prioridad(receta)
            print(f"{idx}. {receta.nombre}")
            print(f"   Calorías: {receta.calorias} | Proteína: {receta.proteina}g | Tiempo: {receta.tiempo_minutos}min")
            print(f"   Prioridad: {prioridad:.4f}\n")
        return top

    def cargar_desde_json(self, ruta):
        import json
        with open(ruta, encoding='utf-8') as f:
            datos = json.load(f)
        for d in datos:
            receta = Receta(
                nombre=d['nombre'],
                tiempo_minutos=d['tiempo_minutos'],
                calorias=d['calorias'],
                proteina=d.get('proteina', 0),
                dificultad=d.get('dificultad', 'Media'),
                ingredientes=d.get('ingredientes', []),
                categoria=d.get('categoria', 'Tradicional')
            )
            self.agregar_receta(receta)
