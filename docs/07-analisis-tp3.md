# Análisis del TP3 — Árbol Binario
Proyecto: GastroRecommender — Grupo 3

## 1. Comparación de formas de buscar

| Qué hacemos | Lista común | Lista ordenada | Con Árbol |
|---|---|---|---|
| Agregar dato | Rápido | Lento | Rápido |
| Buscar dato | Lento, revisa todo | Más rápido | Rápido |
| Ordenar todo | Hay que hacerlo a mano | Ya está ordenada | Se ordena solo |

## 2. Tiempos que medimos

| Cantidad | Secuencial | Binaria | Con Árbol |
|---|---|---|---|
| 100 | *(lo que dé al ejecutar)* | *(lo que dé)* | *(lo que dé)* |
| 1.000 | *(lo que dé)* | *(lo que dé)* | *(lo que dé)* |
| 5.000 | *(lo que dé)* | *(lo que dé)* | *(lo que dé)* |
| 10.000 | *(lo que dé)* | *(lo que dé)* | *(lo que dé)* |
| 50.000 | *(lo que dé)* | *(lo que dé)* | *(lo que dé)* |

> Después ejecutamos el programa y completamos con los números que salgan.

## 3. Por qué elegimos el Árbol

- Con una lista normal, para buscar una receta hay que ir viendo una por una y tarda mucho si hay muchas.
- Con la lista ordenada se busca más rápido, pero cada vez que agregamos algo hay que acomodar todo de nuevo.
- El **Árbol Binario** es lo mejor para nuestro proyecto:
  - Agregamos recetas y se ordenan solas por calorías
  - Buscamos rápido sin tener que revisar todo
    

## 4. Las 3 formas de recorrerlo
- **De menor a mayor** → muestra las recetas de menos calorías a más
- **Empieza por la raíz** → va directo al centro y sigue bajando
- **Termina en la raíz** → recorre todas las ramas y llega al centro al final
