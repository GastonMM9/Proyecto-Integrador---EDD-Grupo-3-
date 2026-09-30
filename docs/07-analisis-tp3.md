# Análisis del TP3 — Árbol Binario
Proyecto: GastroRecommender — Grupo 3

---

## 1. Cómo buscamos de distinta forma

| Qué hacemos | Lista común | Lista ordenada | Con Árbol |
|---|---|---|---|
| Agregar | Rápido | Tengo que acomodar todo | Rápido y se acomoda solo |
| Buscar | Voy uno por uno, tardo mucho | Más rápido | Muy rápido, empiezo del medio |
| Ordenar | Lo hago a mano cada vez | Ya está ordenado | Se ordena solo al cargar |

---

## 2. Por qué elegimos el Árbol

Al principio pensábamos usar lista, pero no nos sirvió:

- Con lista normal, buscar tarda mucho porque reviso todo de a uno
- Con lista ordenada busco más rápido, pero cada vez que agrego algo tengo que reacomodar todo
- El Árbol Binario es mejor para nosotros porque:
  - Las recetas se ordenan solas cuando las cargo
  - Busca rapidísimo, no revisa todo
  - Puedo mostrar ordenado de distintas formas sin tener que rehacer nada

---

## 3. Las tres formas de recorrerlo

| Forma | Qué hace | Para qué sirve |
|---|---|---|
| De menor a mayor | Muestra desde la receta con menos calorías hasta la que tiene más | Ver primero las más livianas |
| Empezando por la raíz | Muestra la del medio primero y después baja | Para guardar todo tal cual está |
| Terminando en la raíz | Recorre las ramas primero y al final la del medio | Si borramos todo, no perdemos nada |
