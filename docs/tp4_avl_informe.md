# TP4 — Árbol AVL: Equilibrio y Eficiencia
**Proyecto:** GastroRecommender

---

## 1. ¿Qué pasa cuando el árbol pierde el equilibrio?
Cuando insertamos recetas **ya ordenadas** (por ejemplo, de la A a la Z por nombre, o de menor a mayor por calorías), el Árbol Binario de Búsqueda común (BST) tiene un problema:

- Todos los elementos van cayendo del mismo lado
- El árbol se va alargando como una **lista enlazada**
- La altura del árbol = cantidad de recetas
- Buscar un elemento puede tardar **O(n)** en vez de O(log n)

Con pocas recetas no se nota, pero a medida que crece el catálogo, el sistema se vuelve **más lento**.

## 2. ¿Cómo soluciona el AVL esto?
El árbol AVL vigila constantemente el **equilibrio** entre sus ramas:

- Calcula la **diferencia de altura** entre la rama izquierda y la derecha → se llama **factor de balance**
- Si esa diferencia es mayor a 1 → el árbol **se desequilibró**
- Entonces aplica una **rotación** para reacomodar las ramas y volver a equilibrarse
- Hay 4 tipos de rotación: simple derecha, simple izquierda, doble izquierda-derecha y doble derecha-izquierda
- El resultado: la altura siempre se mantiene baja → búsqueda en **O(log n)** garantizada

## 3. Experimento — Caso de desbalance
Insertamos recetas en orden alfabético (de la A a la Z):

| Estructura | Altura resultante | Complejidad de búsqueda |
|---|---|---|
| BST común | Igual a la cantidad de recetas → crece mucho | O(n) ❌ |
| AVL | ≈ log₂(cantidad) → siempre compacto | O(log n) ✅ |

**Ejemplo con 10 recetas ordenadas:**
- BST → altura 10 (parece una lista)
- AVL → altura 4 o menos (bien equilibrado)

## 4. ¿Por qué importa en GastroRecommender?
- Si cargamos recetas ordenadas por nombre o por calorías, el BST común se debilita
- El AVL **no importa en qué orden lleguen los datos**, siempre se mantiene equilibrado
- A medida que agreguemos más recetas con el tiempo, el sistema **sigue siendo rápido**
- Es más robusto y confiable para un sistema que va creciendo

## 5. Conclusión técnica
- **BST simple:** funciona bien con datos desordenados, pero se degrada a O(n) si los datos vienen ordenados
- **AVL:** cuesta un poquito más al insertar (por las rotaciones), **pero siempre busca en O(log n)**
- Para GastroRecommender elegimos AVL porque **garantiza rendimiento sin importar el orden de llegada de las recetas**
- Es la opción más sólida para un sistema que va a crecer con el tiempo

---

## ✅ Archivos modificados en este TP
- `modelos/arbol_avl_receta.py` → ✨ Nuevo: implementación completa del árbol AVL
- `servicios/catalogo.py` → integrado AVL al catálogo, manteniendo el BST original
- `ui/terminal.py` → agregadas opciones para ver AVL y comparar con BST
- `docs/tp4_avl_informe.md` → ✨ Este informe
-----
