# TP7 — GRAFOS: GastroRecommender
# Grupo 3 

from collections import deque
import heapq


class GrafoRecetas:
    def __init__(self):
        # Lista de adyacencia
        self.adyacencia = {}

    def conectar_por_calorias(self, nombre1, calorias1, nombre2, calorias2):
        # Similitud: cuanto más parecidas en calorías, mayor conexión
        diferencia = abs(calorias1 - calorias2)
        similitud = max(0, 10 - diferencia // 10)

        # Grafo NO DIRIGIDO
        if nombre1 not in self.adyacencia:
            self.adyacencia[nombre1] = []
        self.adyacencia[nombre1].append((nombre2, similitud))

        if nombre2 not in self.adyacencia:
            self.adyacencia[nombre2] = []
        self.adyacencia[nombre2].append((nombre1, similitud))

    # --- BFS: recetas con calorías parecidas ---
    def recetas_mas_parecidas(self, inicio):
        """Muestra primero las que más se parecen → sirve para tu objetivo"""
        visitados = set([inicio])
        cola = deque([inicio])
        recorrido = []
        while cola:
            actual = cola.popleft()
            recorrido.append(actual)
            for vecino, _ in self.adyacencia[actual]:
                if vecino not in visitados:
                    visitados.add(vecino)
                    cola.append(vecino)
        return recorrido

    # --- DFS: ver todo el grupo ---
    def explorar_relacionadas(self, inicio, visitados=None, recorrido=None):
        if visitados is None:
            visitados = set()
        if recorrido is None:
            recorrido = []
        visitados.add(inicio)
        recorrido.append(inicio)
        for vecino, _ in self.adyacencia[inicio]:
            if vecino not in visitados:
                self.explorar_relacionadas(vecino, visitados, recorrido)
        return recorrido

    # --- Dijkstra: mejor camino ---
    def camino_por_objetivo(self, desde, hasta):
        """Costo = 10 - similitud → menor = mejor para tu meta"""
        cola = [(0, desde, [desde])]
        menor_costo = {}
        while cola:
            costo_act, nodo, camino = heapq.heappop(cola)
            if nodo == hasta:
                return camino, costo_act
            if nodo in menor_costo and menor_costo[nodo] <= costo_act:
                continue
            menor_costo[nodo] = costo_act
            for vecino, sim in self.adyacencia[nodo]:
                costo = 10 - sim
                heapq.heappush(cola, (costo_act + costo, vecino, camino + [vecino]))
        return None, None


# --- PRUEBA con recetas ligadas a tu proyecto ---
if __name__ == "__main__":
    grafo = GrafoRecetas()

    # 2 recetas conectadas por calorías → ligadas a tu objetivo
    grafo.conectar_por_calorias("Milanesa", 250, "Milanesa Napolitana", 280)

    print("✅ Grafo cargado")
    print("Recetas conectadas por calorías:")
    for nombre in grafo.adyacencia:
        print(f"  - {nombre}")

    print("\n🔍 BFS — Más parecidas en calorías:")
    print(" → ".join(grafo.recetas_mas_parecidas("Milanesa")))

    print("\n🌳 DFS — Todas relacionadas:")
    print(" → ".join(grafo.explorar_relacionadas("Milanesa")))

    camino, costo = grafo.camino_por_objetivo("Milanesa", "Milanesa Napolitana")
    print(f"\n⭐ Mejor camino: {' → '.join(camino)}")
    print(f"Costo: {costo} (menor = mejor para tu objetivo)")
