# Proyecto Integrador (GRUPO 3) — GastroRecommender

## Descripción
El sistema GastroRecommender gestiona recetas, ingredientes y menús. Recomienda platos adaptados a distintos objetivos: perder peso, ganar masa muscular y alimentación equilibrada.

## Integrantes
- Gastón Morel
- Daiana Núñez
- Mercedes González

## Cómo ejecutar
1. Clonar el repositorio: https://github.com/GastonMM9/Proyecto-Integrador---EDD-Grupo-3-
2. Ejecutar: `python ui/terminal.py`

---

## Estado de cada trabajo

| Trabajo | Estado |
|---|---|
| TP0 | ✅ Terminado |
| TP1 | ✅ Terminado |
| TP2 | ✅ Cancelado |
| TP3 — Árbol Binario | ✅ Terminado |
| TP4 — Árbol AVL | ✅ Terminado |
| TP5 — Árbol General | ✅ Terminado |
| TP6 — Cola de Prioridad | ✅ Terminado |
| TP7 — Grafos | ⚙️ No se hace (explicación abajo) |
| TP8 — Todo funciona junto | ✅ Terminado, se ejecuta desde terminal |

---

## TP3 — Árbol Binario
Elegimos usar árbol binario de búsqueda para ordenar las recetas por calorías. Así no tenemos que buscar a mano ni revisar todo de a una: el árbol nos da el dato directo y podemos filtrar por rango de calorías de forma rápida.

## TP4 — Árbol AVL
Hicimos un árbol que se mantiene siempre equilibrado. Ninguna rama crece más que otra. Esto hace que buscar sea siempre rápido, aunque guardemos muchas recetas. Creamos dos árboles: uno ordena por nombre y otro por calorías.

## TP5 — Árbol General
Organizamos las recetas por categorías, como si fuera un menú con carpetas. Cada rama puede tener la cantidad de hijos que necesite. Recorremos de dos formas: por amplitud (nivel por nivel) y por profundidad (rama por rama). Cada receta tiene una puntuación que combina: menos calorías, más proteína y menos tiempo de preparación → así sabemos cuál es la mejor.

## TP6 — Cola de Prioridad
Usamos Heap porque no necesitamos ordenar todo. Solo pedimos las 5 mejores recetas y el programa nos las da directo, sin mirar las demás. Es rápido y eficiente.

## TP7 — Sobre los Grafos
Decidimos **no hacer la parte de grafos** porque todo lo que necesitamos ya lo tenemos hecho:
- Buscamos por calorías → Árbol Binario
- Ordenamos rápido → Árbol AVL
- Agrupamos por categorías → Árbol General
- Recomendamos según meta → Cola de Prioridad

