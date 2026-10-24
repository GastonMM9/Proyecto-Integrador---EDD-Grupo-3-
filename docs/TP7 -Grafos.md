# TP7 — Grafos: Decisión de Diseño
## GastroRecommender — Grupo 3

### Decisión
Se evaluó incorporar un modelo de grafos, pero se determinó que **no es necesario** para cumplir los objetivos del sistema.

### Motivos
1. Las relaciones entre recetas ya se manejan con las estructuras anteriores:
   - Búsqueda por calorías → Árbol Binario (TP3)
   - Ordenamiento equilibrado → Árbol AVL (TP4)
   - Categorías → Árbol General (TP5)
   - Recomendaciones por objetivo → Cola de Prioridad (TP6)

2. Un grafo no aportaría funcionalidad nueva, solo duplicaría información que ya existe por categoría, calorías e ingredientes.

3. Se prefiere mantener el sistema simple, funcional y sin complejidad innecesaria.

### Conclusión
El proyecto cumple todos los requisitos con las estructuras ya implementadas. Por eso se decide no incorporar grafos.
