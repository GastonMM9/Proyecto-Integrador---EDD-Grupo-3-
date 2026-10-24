# TP7 — Grafos
## GastroRecommender — Grupo 3

### Conexión con el proyecto
En los trabajos anteriores trabajamos con:
- **TP3:** buscar y ordenar recetas por calorías
- **TP4:** comparar estructuras para buscar rápido
- **TP5:** organizar recetas por categorías
- **TP6:** recomendar según objetivo (perder peso / ganar masa)

Ahora con grafos conectamos recetas que tienen calorías parecidas, para recomendarte otras que van con tu misma meta.

### 1. Definiciones
- **Vértices:** las recetas
  - "Milanesa" → 250 kcal
  - "Milanesa Napolitana" → 280 kcal
- **Aristas:** se conectan porque tienen calorías cercanas
  - Similitud: 7/10
- **Tipo de grafo:** No dirigido + pesado
  - No dirigido: la relación va en los dos sentidos
  - Pesado: el valor cambia según qué tan parecidas sean
- **Representación:** Lista de adyacencia
  - Justificación: hay pocas conexiones, ocupa menos memoria que la matriz

### 2. Recorridos
- **BFS:** muestra primero las recetas más parecidas en calorías
  - *Para qué sirve:* "Me gusta esta receta → mostrame otras parecidas"
  - Complejidad: O(V + E)

- **DFS:** muestra todas las recetas relacionadas
  - *Para qué sirve:* "Quiero ver todo lo que se parece a esta"
  - Complejidad: O(V + E)

### 3. Mejor camino — Dijkstra
- **Costo:** 10 − similitud → cuanto menor, más se parecen en calorías
- **Por qué Dijkstra:** todos los valores son positivos
- **Complejidad:** O(E log V)

### 4. Salida del programa
