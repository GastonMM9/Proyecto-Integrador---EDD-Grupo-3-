# GastroRecommender — Propuesta (TP0)

**Es un sistema de clasificacion de alimentos, control de stock y recetario.  
Diseñado para facilitar la elavoracion de recetas de nuestro interes dependiendo de nuestros alimentos disponibles.**

## 1. Dominio elegido y justificación

**Dominio: Gastronomia.**  

Es un tema que decidimos entre los integrantes del grupo, ya que es un problema en comun que tenemos a la hora de llegar de trabajar cansados y con poco tiempo.

## 2. Problema que resuelve

- La falta de tiempo.
- El desperdicio de comida por contar con ingredientes limitados en la heladera.
- La dificultad de adaptar la alimentaciòn a metas nutricionales especificas.

## 3. Usuario objetivo

- Personas que cocinan en su hogar con poco tiempo o insumos contados, y usuarios interesados en controlar su ingesta calòrica o   macronutrientes (ganancia de masa muscular, descenso de peso, etc.)

## 4. Funcionalidades iniciales

- Registrar, modificar y eliminar recetas.
- Administrar ingredientes, cantidades y disponibilidad.
- Clasificar recetas según objetivo: pérdida de peso, aumento de masa muscular y platos equilibrados o saludables.
- Armar platos y menús completos adaptados a cada meta.
- Buscar y recomendar según gustos, ingredientes disponibles y tipo de alimentación.
- Guardar, ordenar y cargar toda la información.

| ID | GastroRecommender |
|---|---|
| F1 | Stock de ingredientes |
| F2 | Lista de recetas  | 
| F3 | Recomendaciones |
| F4 | Recordatorio de compra |
| F5 | Vencimientos |

## 5. Ejemplo de uso (input/output)

```text
========================================
 GastroRecommender — TERMINAL
========================================
1. Stock de ingredientes
2. Lista de recetas
3. Recomendaciones
4. Recordatorio de compra
5. Vencimientos
0. Salir

----------------------------------------

Opción: 5

========================================
 GastroRecommender — Vencimientos
========================================

Pollo vence en (3 días).
Dulce de leche vence en (13 Días).
Tomate vence en (5 días).


```


