# Proyecto Integrador (GRUPO 3) — GastroRecommender
### Descripción

 Sistema **GastroRecommender**: gestiona recetas, ingredientes, menús y recomienda platos adaptados a distintos objetivos como por ejemplo perdida de peso,aumento de masa muscular y alimentacion equilibrada

### Integrantes

- Gastón Morel
- Daiana Nuñez
- Mercedes González 

## Cómo ejecutar 
1. Clonar el repositorio https://github.com/GastonMM9/Proyecto-Integrador---EDD-Grupo-3-
2. Ejecutar: python ui/terminal.py 

## Estado 
- TP0: Completado 
- TP1: Completado - *Pendiente para posibles cambios*
- TP2: Completado - *Cancelado*
- TP3: Para revisión 
-TP3: Árbol binario de búsqueda elegimos usar esta estructura porque:
  **Ordenar automáticamente las recetas por calorías, sin tener que ordenarlas a mano.
  **Buscar mas rapido en lugar de revisar una por una, el arbol va directo al dato que buscamos.
  **Filtrar por rango podemos buscar receta entre ciertos valores de calorias de forma eficiente. 
 
 ## Trabajo Práctico 4 — Árbol AVL

### ¿Qué hicimos?
Implementamos un tipo de árbol binario que se mantiene siempre equilibrado. Esto quiere decir que sus ramas no crecen de un solo lado, sino que se van acomodando solas para mantenerse parejo.

### ¿Para qué sirve?
- Permite buscar recetas mucho más rápido que en un árbol común
- Si el árbol está equilibrado, ninguna rama se hace muy larga
- Funciona igual de rápido aunque tengamos muchísimas recetas guardadas

### Lo que hicimos:
- Creamos dos árboles AVL: uno ordena por **nombre** y otro por **calorías**
- Agregamos opciones en el menú para ver las recetas ordenadas con estos árboles
- Comparamos la altura del árbol normal contra el AVL y vimos que el AVL es mucho más bajo y equilibrado ✅

---

## Trabajo Práctico 5 — Árbol General

### ¿Qué hicimos?
Creamos una estructura para organizar las recetas por **categorías**, como si fuera un menú con carpetas y subcarpetas. A diferencia de los árboles anteriores, cada rama puede tener la cantidad de hijos que necesite.

### ¿Para qué sirve?
- Agrupamos las recetas en: Saludable, Rápida y Tradicional
- Se puede ver la estructura completa de las categorías
- Permite recorrer y listar qué hay dentro de cada categoría

### Lo que hicimos:
- Definimos la estructura principal: Categorías → Subcategorías → Recetas
- Agregamos dos formas de recorrerlo:
  - **Por amplitud**: muestra todo lo que hay en un nivel antes de bajar al siguiente
  - **Por profundidad**: baja hasta el final de cada rama antes de pasar a la siguiente
- Cada receta que se carga se asigna automáticamente a su categoría correspondiente
  -TP6: GastroRecommender — TP6: Colas de Prioridad

  1. ¿Cómo definimos qué receta es mejor?
Creamos una "puntuación" que combina tres cosas:
- Menos calorías → mejor puntuación
- Más proteína → mejor puntuaciónuchas
- Menos tiempo de preparación → mejor puntuación

Cada receta tiene un número de prioridad: cuanto más alto, más recomendada.

 2. ¿Qué hicimos en el código?
- Programamos desde cero una estructura que se llama **Heap Binario**, sin usar librerías ya hechas
- Cada vez que se carga una receta nueva, se guarda automáticamente en esta estructura
- Agregamos la **opción 13** en el menú: al elegirla te muestra las N recetas con mayor puntuación
- Todo lo que ya teníamos de TP3, TP4 y TP5 sigue funcionando igual

## 3. ¿Por qué usamos Heap y no ordenamos todo?
 Tenemos muchas recetas guardadas:
 -Si no usamos Heap ordenamos todo:
- Cada vez que querés ver el Top 5, el programa tiene que ordenar las recetas completas.
- Ordena recetas que ni vas a mirar.
- Si hay muchas recetas, se pone lento.

✅ Si usamos Heap:
- Las recetas se van acomodando solas a medida que se cargan.
- Cuando pedís el Top 5, solo sacás las 5 que están arriba. No mirás las otras 995.
- Siempre es rápido, aunque tengas muchísimas recetas.

**En resumen**: no necesitamos saber el orden de todas las recetas, solo las mejores. El Heap hace exactamente eso y nada más.

## 4. Lo que entregamos
- ✅ Heap binario hecho desde cero
- ✅ Fórmula para calcular la prioridad de cada receta
- ✅ Opción 13 del menú para ver el Top-N
  
