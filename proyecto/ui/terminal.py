import sys
import os

ruta_base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ruta_base)

from servicios.Catalogo import CatalogoRecetas

def mostrar_menu():
    print("=" * 50)
    print("     GASTRORECOMMENDER - TP3 ÁRBOL BINARIO")
    print("=" * 50)
    print(" 1 - Cargar recetas desde JSON")
    print(" 2 - Listar todas las recetas")
    print(" 3 - Listar ordenadas por calorías")
    print(" 4 - Recorrido PREORDEN")
    print(" 5 - Recorrido POSTORDEN")
    print(" 6 - Buscar receta por nombre")
    print(" 7 - Salir")
    print("=" * 50)

def main():
    catalogo = CatalogoRecetas()
    cargado = False

    while True:
        mostrar_menu()
        opcion = input("Elegí una opción: ")

        if opcion == "1":
            try:
                catalogo.cargar_desde_json()
                print("✅ Recetas cargadas correctamente!")
                cargado = True
            except Exception as e:
                print(f"❌ Error al cargar: {e}")

        elif opcion == "2":
            if not cargado:
                print("⚠️ Primero cargá las recetas (opción 1)")
                continue
            recetas = catalogo.listar_todos()
            print(f"\n📋 Total: {len(recetas)} recetas")
            for r in recetas:
                print(f"  - {r}")

        elif opcion == "3":
            if not cargado:
                print("⚠️ Primero cargá las recetas (opción 1)")
                continue
            recetas = catalogo.listar_ordenados()
            print(f"\n📋 Ordenadas por calorías:")
            for r in recetas:
                print(f"  - {r}")

        elif opcion == "4":
            if not cargado:
                print("⚠️ Primero cargá las recetas (opción 1)")
                continue
            recetas = catalogo.listar_preorden()
            print(f"\n🌿 Recorrido PREORDEN:")
            for r in recetas:
                print(f"  - {r}")

        elif opcion == "5":
            if not cargado:
                print("⚠️ Primero cargá las recetas (opción 1)")
                continue
            recetas = catalogo.listar_postorden()
            print(f"\n🍂 Recorrido POSTORDEN:")
            for r in recetas:
                print(f"  - {r}")

        elif opcion == "6":
            if not cargado:
                print("⚠️ Primero cargá las recetas (opción 1)")
                continue
            busqueda = input("Escribí el nombre a buscar: ")
            resultados = catalogo.buscar(busqueda)
            if resultados:
                print(f"\n🔍 Encontré {len(resultados)} receta(s):")
                for r in resultados:
                    print(f"  - {r}")
            else:
                print("⚠️ No se encontraron recetas")

        elif opcion == "7":
            print("👋 ¡Gracias!")
            break

        else:
            print("❌ Opción inválida")
        
        input("\nPresioná Enter para continuar...")
        os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    main()
