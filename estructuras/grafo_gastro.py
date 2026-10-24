# TP7 — GRAFOS: GastroRecommender
# Grupo 3 — Integración con catálogo real

from collections import deque
import heapq


class GrafoRecetas:
    def __init__(self):
        self.adyacencia = {}

    def conectar_desde_catalogo(self, lista_recetas):
        """Construye el grafo con TODAS las recetas cargadas"""
        self.adyacencia = {}

        def calcular_similitud(r1, r2):
            # Por calorías → base de nuestro proyecto
            diferencia = abs(r1.calorias - r2.calorias)
            sim_cal = max(0, 5 - diferencia // 50)

            # Por categoría
            sim_cat = 3 if getattr(r1, 'categoria', '') == getattr(r2, 'categoria', '') else 0

            # Por ingredientes
            ing1 = set(getattr(r1, 'ingredientes', []))
            ing2 = set(getattr(r2, 'ingredientes', []))
            sim_ing = min(len(ing1 & ing2), 2)

            return sim_cal + sim_cat + sim_ing

        # Conectar recetas relacionadas
        for i in range(len(lista_recetas)):
            for j in range(i + 1, len(lista_recetas)):
                r1 = lista_recetas[i]
                r2 = lista_recetas[j]
                sim = calcular_similitud(r1, r2)
                if sim >= 4:  # Solo conectar si son parecidas
                    self._agregar_arista(r1.nombre, r2.nombre, sim)

    def _agregar_arista(self, a, b, valor):
        if a not in self.adyacencia:
            self.adyacencia[a] = []
        self.adyacencia[a].append((b, valor))
        if b not in self.adyacencia:
            self.adyacencia[b] = []
        self.adyacencia[b].append((a, valor))

    # --- BFS ---
    def bfs(self, inicio):
        if inicio not in self.adyacencia:
            return [f"'{inicio}' no encontrada"]
        visitados = set([inicio])
        cola = deque([inicio])
        res = []
        while cola:
            act = cola.popleft()
            res.append(act)
            for vec, _ in self.adyacencia[act]:
                if vec not in visitados:
                    visitados.add(vec)
                    cola.append(vec)
        return res

    # --- DFS ---
    def dfs(self, inicio, vis=None, res=None):
        if vis is None: vis = set()
        if res is None: res = []
        if inicio not in self.adyacencia or inicio in vis:
            return res
        vis.add(inicio)
        res.append(inicio)
        for vec, _ in self.adyacencia[inicio]:
            if vec not in vis:
                self.dfs(vec, vis, res)
        return res

    # --- Camino mínimo — Dijkstra ---
    def camino_minimo(self, desde, hasta):
        # Costo = 10 - similitud → menor = mejor
        cola = [(0, desde, [desde])]
        mejores = {}
        while cola:
            costo_act, nodo, camino = heapq.heappop(cola)
            if nodo == hasta:
                return {"camino": camino, "costo": costo_act}
            if nodo in mejores and mejores[nodo] <= costo_act:
                continue
            mejores[nodo] = costo_act
            for vec, sim in self.adyacencia.get(nodo, []):
                nuevo_costo = costo_act + (10 - sim)
                heapq.heappush(cola, (nuevo_costo, vec, camino + [vec]))
        return None
