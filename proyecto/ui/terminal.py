import sys
sys.path.insert(0, '.')

from servicios.Catalogo import CatalogoRecetas

def mostrar_menu():
    print("=" * 50)
    print("   GASTRORECOMMENDER - TP3 ÁRBOL BINARIO")
    print("=" * 50)
    print("1. Cargar recetas desde archivo")
    print("2. Listar todas las recetas")
    print("3. Listar ordenadas por calorías (Árbol)")
    print("4. Buscar por rango de calorías")
    print("5. Salir")
    print("=" * 50)
    return input("Elegí una opción: ")

def main():
    catalogo = CatalogoRecetas()
    
    while True:
        opcion = mostrar_menu()
        
        if opcion == "1":
            catalogo.cargar_desde_json("datos/ingredientes_y_recetas.json")
            print("✅ Recetas cargadas correctamente")
        
        elif opcion == "2":
            print("\n📋 Lista de todas las recetas:")
            for r in catalogo.listar_todas():
                print(f"  - {r.nombre} | {r.calorias} kcal")
        
        elif opcion == "3":
            print("\n🌳 Ordenadas por calorías (Árbol Binario):")
            for r in catalogo.listar_ordenadas_por_calorias():
                print(f"  - {r.nombre} | {r.calorias} kcal")
        
        elif opcion == "4":
            min_cal = int(input("Calorías mínimas: "))
            max_cal = int(input("Calorías máximas: "))
            print(f"\n🔍 Resultados entre {min_cal} y {max_cal} kcal:")
            for r in catalogo.buscar_por_calorias(min_cal, max_cal):
                print(f"  - {r.nombre} | {r.calorias} kcal")
        
        elif opcion == "5":
            print("👋 ¡Hasta luego!")
            break
        
        input("\nPresioná Enter para continuar...")

if __name__ == "__main__":
    main()
