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
            print("¡Hasta luego!")
            break
        elif opcion == "1":
            print("Recetas cargadas correctamente ✅")
        elif opcion == "2":
            print("Búsqueda por calorías — En desarrollo 🚧")
        elif opcion == "3":
            print("Recomendaciones por prioridad — En desarrollo 🚧")
        else:
            print("Opción inválida. Intentá nuevamente.")


if __name__ == "__main__":
    main()
