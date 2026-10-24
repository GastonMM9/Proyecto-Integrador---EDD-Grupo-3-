import sys
sys.path.append("..")

from servicios.Catalogo import Catalogo


def main():
    catalogo = Catalogo()
    catalogo.cargar_desde_json("datos/ingredientes_recetas.json")

    while True:
        print("\n" + "=" * 50)
        print("       GASTRO RECOMMENDER")
        print("=" * 50)
        print("1. Cargar recetas")
        print("2. Buscar recetas por calorías")
        print("3. Recomendaciones por prioridad")
        print("0. Salir")

        opcion = input("\nElegí una opción: ")

        if opcion == "0":
            print(" ¡Hasta luego!")
            break
        else:
            print(" Opción en desarrollo")


if __name__ == "__main__":
    main()
