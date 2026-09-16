import sys
sys.path.insert(0, '.')
from estructuras.arbol_binario import ArbolBinarioBusqueda

def main():
    print("=== PRUEBA ÁRBOL BINARIO DE BÚSQUEDA ===")
    arbol = ArbolBinarioBusqueda()
    valores = [50, 30, 70, 20, 40, 60, 80]
    
    print(f"\nInsertando valores: {valores}")
    for v in valores:
        arbol.insertar(v)
    
    print("\n✅ Recorrido INORDEN  :", arbol.inorden())
    print("✅ Recorrido PREORDEN :", arbol.preorden())
    print("✅ Recorrido POSTORDEN:", arbol.postorden())
    
    buscar = 40
    resultado = arbol.buscar(buscar)
    print(f"\n🔍 Buscar {buscar}: {resultado if resultado else 'No encontrado'}")
    
    buscar = 99
    resultado = arbol.buscar(buscar)
    print(f"🔍 Buscar {buscar}: {resultado if resultado else 'No encontrado'}")
    
    print("\n✅ Prueba finalizada")

if __name__ == "__main__":
    main()
