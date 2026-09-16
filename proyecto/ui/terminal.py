import sys
sys.path.insert(0, '.')

from servicios.Catalogo import CatalogoRecetas

def mostrar_menu():
    print("=" * 55)
    print("   GASTRORECOMMENDER — TP3 ÁRBOL BINARIO")
    print("=" * 55)
    print("1. Cargar recetas desde archivo")
    print("2. Listar todas (lista normal)")
    print("3. Listar ordenadas por calorías (INORDEN)")
    print("4. Ver recorrido PREORDEN")
    print("5. Ver recorrido POSTORDEN")
    print("6. Buscar por caloría exacta (usa Árbol)")
    print("7. Salir")
    print("=" * 55)
    return input("Elegí una opción: ")

def main():
    catalogo = CatalogoRecetas()
    
    while True:
        opcion = mostrar_menu()
        
        if opcion == "1":
            catalogo.cargar_desde_json("datos/ingredientes_y_recetas.json")
            print("✅ Recetas cargadas")
        
        elif opcion == "2":
            print("\n📋 Lista completa:")
            for r in catalogo.listar_todas():
                print(f"  - {r.nombre} | {r.calorias} kcal")
        
        elif opcion == "3":
            print("\n🌳 Ordenadas de menor a mayor caloría:")
            cal = catalogo.listar_inorden()
            print(f"  Calorías: {cal}")
        
        elif opcion == "4":
            print("\n🌳 Recorrido PREORDEN:")
            cal = catalogo.listar_preorden()
            print(f"  Calorías: {cal}")
        
        elif opcion == "5":
            print("\n🌳 Recorrido POSTORDEN:")
            cal = catalogo.listar_postorden()
            print(f"  Calorías: {cal}")
        
        elif opcion == "6":
            valor = int(input("Caloría a buscar: "))
            res = catalogo.buscar_por_calorias_arbol(valor)
            if res:
                print(f"✅ Encontrado: {res} kcal")
            else:
                print("❌ No encontrado")
        
        elif opcion == "7":
            print("👋 ¡Hasta luego!")
            break
        
        input("\nEnter para continuar...")

if __name__ == "__main__":
    main()
