import sys
sys.path.insert(0, '.')

from servicios.Catalogo import CatalogoRecetas

def mostrar_menu():
    print("=" * 55)
    print("   GASTRORECOMMENDER — TP3 + TP4 + TP5")
    print("=" * 55)
    print("--- TP3: ARBOL BINARIO ---")
    print("1. Cargar recetas desde archivo")
    print("2. Listar todas")
    print("3. Listar ordenadas por calorias (INORDEN)")
    print("4. Ver recorrido PREORDEN")
    print("5. Ver recorrido POSTORDEN")
    print("6. Buscar por caloria exacta")
    print("--- TP4: ARBOL AVL ---")
    print("8. Ordenar por nombre (AVL)")
    print("9. Ordenar por calorias (AVL)")
    print("10. Comparar alturas: BST vs AVL")
    print("--- TP5: ARBOL GENERAL ---")
    print("11. Ver categorias — recorrido por amplitud")
    print("12. Ver categorias — recorrido por profundidad")
    print("7. Salir")
    print("=" * 55)
    return input("Elegi una opcion: ")

def main():
    catalogo = CatalogoRecetas()
    
    while True:
        opcion = mostrar_menu()
        
        if opcion == "1":
            catalogo.cargar_desde_json("datos/ingredientes_y_recetas.json")
            print("Recetas cargadas")
        
        elif opcion == "2":
            print("\nLista completa:")
            for r in catalogo.listar_todas():
                print(f"  - {r.nombre} | {r.calorias} kcal")
        
        elif opcion == "3":
            print("\nOrdenadas de menor a mayor caloria:")
            cal = catalogo.listar_inorden()
            print(f"  Calorias: {cal}")
        
        elif opcion == "4":
            print("\nRecorrido PREORDEN:")
            cal = catalogo.listar_preorden()
            print(f"  Calorias: {cal}")
        
        elif opcion == "5":
            print("\nRecorrido POSTORDEN:")
            cal = catalogo.listar_postorden()
            print(f"  Calorias: {cal}")
        
        elif opcion == "6":
            valor = int(input("Caloria a buscar: "))
            res = catalogo.buscar_por_calorias_arbol(valor)
            if res:
                print(f"Encontrado: {res} kcal")
            else:
                print("No encontrado")
        
        elif opcion == "8":
            print("\nAVL — Ordenado por nombre:")
            for receta in catalogo.arbol_avl_nombre.inorder():
                print(f"  - {receta.nombre}")
        
        elif opcion == "9":
            print("\nAVL — Ordenado por calorias:")
            for receta in catalogo.arbol_avl_calorias.inorder():
                print(f"  - {receta.nombre}: {receta.calorias} kcal")
        
        elif opcion == "10":
            print("\nCOMPARACION: BST vs AVL")
            print(f"BST por calorias — Altura: {catalogo.arbol_calorias.altura()}")
            print(f"AVL por calorias — Altura: {catalogo.arbol_avl_calorias.altura()}")
            print(f"BST por nombre   — Altura: {catalogo.arbol_nombre.altura()}")
            print(f"AVL por nombre   — Altura: {catalogo.arbol_avl_nombre.altura()}")
            print("\nDiferencia: AVL mantiene la altura baja = busquedas mas rapidas")
        
        elif opcion == "11":
            print("\nCategorias — Recorrido por amplitud:")
            for elemento in catalogo.recorrer_por_amplitud():
                print(f"  - {elemento}")
        
        elif opcion == "12":
            print("\nCategorias — Recorrido por profundidad:")
            for elemento in catalogo.recorrer_por_profundidad():
                print(f"  - {elemento}")
        
        elif opcion == "7":
            print("Hasta luego")
            break
        
        input("\nEnter para continuar...")

if __name__ == "__main__":
    main()
