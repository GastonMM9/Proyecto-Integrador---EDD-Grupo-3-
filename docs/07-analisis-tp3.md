# Análisis del TP3 — Árbol Binario

**Proyecto:** GastroRecommender — Grupo 3

---

## 1. Cómo buscamos de distinta forma

- **Lista común**
  - Agregar: Rápido
  - Buscar: Voy uno por uno, tardo mucho
  - Ordenar: Lo hago a mano cada vez

- **Lista ordenada**
  - Agregar: Tengo que acomodar todo
  - Buscar: Más rápido
  - Ordenar: Ya está ordenado

- **Con Árbol Binario**
  - Agregar: Rápido y se acomoda solo
  - Buscar: Muy rápido, empiezo del medio
  - Ordenar: Se ordena solo al cargar

---

## 2. Por qué elegimos el Árbol

Al principio pensábamos usar lista, pero no nos sirvió:
- Con lista normal, buscar tarda mucho porque reviso todo de a uno.
- Con lista ordenada busco más rápido, pero cada vez que agrego algo tengo que reacomodar todo.

Elegimos el **Árbol Binario** porque:
- Las recetas se ordenan solas cuando las cargo.
- Busca rapidísimo, no revisa todo.
- Puedo mostrar ordenado de distintas formas sin tener que rehacer nada.

---

## 3. Las tres formas de recorrerlo

- **De menor a mayor**
  - Qué hace: Muestra desde la receta con menos calorías hasta la que tiene más
  - Para qué sirve: Ver primero las más livianas

- **Empezando por la raíz**
  - Qué hace: Muestra la del medio primero y después baja
  - Para qué sirve: Para guardar todo tal cual está

- **Terminando en la raíz**
  - Qué hace: Recorre las ramas primero y al final la del medio
  - Para qué sirve: Si borramos todo, no perdemos nada
