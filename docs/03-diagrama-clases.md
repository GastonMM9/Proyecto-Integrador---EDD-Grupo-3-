# 03 — Diagrama de Clases — GastroRecommender

## Clases principales

| Clase | Atributos y responsabilidad |
|---|---|
| **Receta** | código, nombre, pasos, tiempo de preparación, dificultad, objetivo de alimentación, calorías, proteínas, carbohidratos y grasas por porción. |
| **Ingrediente** | nombre, cantidad, unidad de medida, existencias disponibles, calorías y nutrientes cada 100 g. |
| **Plato** | nombre, tipo de plato, lista de recetas que lo componen. |
| **Gestor** | guarda información, ordena, compara el stock de ingredientes, busca recetas y recomienda opciones según la meta elegida. |
