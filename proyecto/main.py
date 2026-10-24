# GASTRO RECOMMENDER — Archivo principal
import sys
sys.path.append("..")

from servicios.Catalogo import Catalogo
from estructuras.grafo_gastro import GrafoRecetas


def main():
    # Cargar catálogo con tus recetas
    catalogo = Catalogo()
    catalogo.cargar_desde_json("datos/ingredientes_recetas.json")

    # Inicializar el grafo
    grafo = GrafoRecetas()

    while True:
        print("\n" + "=" * 50)
        print("       GASTRO RECOMMENDER")
        print("=" * 50)
        print("1. Cargar recetas")
        print("2. Buscar recetas por calorías")
        print("3. Recomendaciones por prioridad")
        print("\n--- TP7: GRAFO ---")
        print("13. Construir red de recetas")
        print("14. Recomendaciones BFS")
        print("15. Explorar con DFS")
        print("16. Camino mínimo entre recetas")
        print("0. Salir")

        opcion = input("\nElegí una opción: ")

        if opcion == "0":
            print(" ¡Hasta luego!")
            break

        elif opcion == "13":
            grafo.conectar_desde_catalogo(catalogo.lista_recetas)
            print(f" Grafo construido — {len(grafo.adyacencia)} recetas conectadas")

        elif opcion == "14":
            nombre = input("Nombre de la receta de inicio: ")
            print("\n Recetas más parecidas:")
            print(" → ".join(grafo.bfs(nombre)))

        elif opcion == "15":
            nombre = input("Nombre de la receta de inicio: ")
            print("\n Todas las relacionadas:")
            print(" → ".join(grafo.dfs(nombre)))

        elif opcion == "16":
            desde = input("Desde receta: ")
            hasta = input("Hasta receta: ")
            resultado = grafo.camino_minimo(desde, hasta)
            if resultado:
                print("\n Mejor camino:")
                print(" → ".join(resultado["camino"]))
                print(f"Costo total: {resultado['costo']}")
            else:
                print(" No hay conexión entre esas recetas")

        else:
            print(" Opción en desarrollo")


if __name__ == "__main__":
    main()
