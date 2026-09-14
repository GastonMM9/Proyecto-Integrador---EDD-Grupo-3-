import sys
sys.path.insert(0,'.')

from servicios.Catalogo import CatalogoRecetas

def mostrar_menu():
    print("=" * 40)
    print("     GASTRO RECOMMENDER - TP3")
    print("   Árbol Binario de Búsqueda")
    print("=" * 40)
    print("1. Cargar recetas desde JSON")
    print("2. Listar todas las recetas")
    print("3. Buscar por calorías")
    print("4. Listar ordenadas por calorías")
    print("5. Salir")
    print("=" * 40)
    return input("Elegí una opción: ")

def main():
    catalogo = CatalogoRecetas()
    cargado = False

    while True:
        opcion = mostrar_menu()

        if opcion == "1":
            ruta = "datos/recetas.json"
            if catalogo.cargar_desde_json(ruta):
                print(" Recetas cargadas correctamente")
                cargado = True
            else:
                print(" No se pudieron cargar los datos")

        elif opcion == "2":
            if not cargado:
                print(" Primero cargá las recetas (opción 1)")
                continue
            print("\n Lista de recetas:")
            for r in catalogo.listar_todas():
                print(f"  - {r}")

        elif opcion == "3":
            if not cargado:
                print(" Primero cargá las recetas (opción 1)")
                continue
            try:
                valor = int(input("Ingresá calorías a buscar: "))
                resultado = catalogo.buscar_por_calorias(valor)
                if resultado:
                    print(f" Encontrada: {resultado}")
                else:
                    print(" No se encontró")
            except ValueError:
                print(" Escribí un número válido")

        elif opcion == "4":
            if not cargado:
                print(" Primero cargá las recetas (opción 1)")
                continue
            print("\n Recetas ordenadas por calorías:")
            for r in catalogo.arbol_calorias.inorden():
                print(f"  - {r}")

        elif opcion == "5":
            print(" ¡Hasta la próxima!")
            break

        else:
            print(" Opción inválida")
        print()

if __name__ == "__main__":
    main()
