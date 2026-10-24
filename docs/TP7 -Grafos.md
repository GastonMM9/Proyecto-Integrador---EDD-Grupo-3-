# TP7 — Grafos: Decisión de Diseño

## GastroRecommender — Grupo 3

---

## Decisión

Se evaluó incorporar un modelo de grafos para representar las relaciones entre recetas, pero después de analizarlo en profundidad, se determinó que **no es necesario ni conveniente** para cumplir los objetivos del sistema.

---

## Motivos

### 1. Toda la funcionalidad ya está cubierta con las estructuras elegidas
Cada necesidad del sistema tiene una solución ya implementada y probada:

| Necesidad del sistema | Estructura que lo resuelve |
|---|---|
| Buscar y filtrar recetas por rango de calorías | Árbol Binario de Búsqueda (TP3) |
| Mantener búsquedas rápidas sin importar el orden de llegada de datos | Árbol AVL (TP4) |
| Organizar recetas por categorías y objetivos nutricionales | Árbol General (TP5) |
| Obtener las mejores recomendaciones según prioridad | Cola de Prioridad — Heap Binario (TP6) |

Ninguna de estas funcionalidades se vería mejorada por un grafo; al contrario, se duplicarían estructuras que ya funcionan correctamente.

### 2. Un grafo no aporta información nueva
Para armar un grafo de recetas habría que definir **conexiones** entre cada par de recetas basándose en:
- Similitud por cantidad de calorías
- Coincidencia de categoría
- Ingredientes compartidos

**Estos mismos criterios ya se usan** en los árboles y en la cola de prioridad. Agregar un grafo sería repetir la misma información de otra forma, sin agregar valor real al usuario.

### 3. Aumentaría la complejidad sin beneficio
- Un grafo requiere gestionar nodos y aristas por separado → más código, más pruebas, más mantenimiento
- Habría que mantener sincronizados el grafo con el catálogo: cada vez que se agrega, modifica o elimina una receta, habría que actualizar todas sus conexiones
- Los recorridos BFS y DFS no aportan nada que no se haga ya con los recorridos de los árboles
- El camino mínimo (Dijkstra) no tiene sentido práctico en este dominio: no existe una "distancia" real entre recetas, solo similitud, que ya se calcula en la cola de prioridad

### 4. El sistema debe ser claro y mantenible
Se prioriza un diseño **sencillo, directo y fácil de entender**. Cada estructura tiene un propósito claro y único:
- Cada estructura cumple una función específica y no se superponen responsabilidades
- Quien lea el código va a entender qué hace cada parte sin confusión
- Se evita el riesgo de inconsistencias entre estructuras paralelas

### 5. Escalabilidad real
Las estructuras elegidas escalan bien con el crecimiento del catálogo:
- Búsqueda en árboles: **O(log n)** garantizada
- Cola de prioridad: obtener las mejores recetas en **O(n log n)** sin ordenar todo
- Un grafo no mejoraría estos tiempos, sino que agregaría peso al sistema

---

## Conclusión

El proyecto cumple **todos los requisitos funcionales y de rendimiento** con las estructuras ya implementadas. La decisión de no incorporar grafos no significa que se haya descartado por falta de conocimiento: se analizó, se comprendió su funcionamiento y se determinó que **no es la herramienta adecuada** para este dominio específico.

Se prefiere un sistema **limpio, eficiente y coherente**, donde cada componente cumple su función sin duplicaciones ni complejidad innecesaria. El código del grafo desarrollado se mantiene en el repositorio como trabajo realizado, pero no se integra al programa final por los motivos expuestos.
