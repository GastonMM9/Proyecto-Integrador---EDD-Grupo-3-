import sys
import time
import random
sys.path.insert(0, '.')
from estructuras.arbol_binario import ArbolBinarioBusqueda

def busqueda_secuencial(lista, valor):
    for elemento in lista:
        if elemento == valor:
            return elemento
    return None

def busqueda_binaria(lista_ordenada, valor):
    izq, der = 0, len(lista_ordenada) - 1
    while izq <= der:
        medio = (izq + der) // 2
        if lista_ordenada[medio] == valor:
            return lista_ordenada[medio]
        elif lista_ordenada[medio] < valor:
            izq = medio + 1
        else:
            der = medio - 1
    return None

def busqueda_arbol(arbol, valor):
    return arbol.buscar(valor)

def medir_tiempos(tamaño):
    datos = random.sample(range(tamaño * 3), tamaño)
    dato_buscar = datos[tamaño // 2]

    lista = datos.copy()
    lista_ordenada = sorted(lista)

    arbol = ArbolBinarioBusqueda()
    for v in lista:
        arbol.insertar(v)

    t0 = time.perf_counter()
    busqueda_secuencial(lista, dato_buscar)
    t_sec = time.perf_counter() - t0

    t0 = time.perf_counter()
    busqueda_binaria(lista_ordenada, dato_buscar)
    t_bin = time.perf_counter() - t0

    t0 = time.perf_counter()
    busqueda_arbol(arbol, dato_buscar)
    t_arbol = time.perf_counter() - t0

    return t_sec, t_bin, t_arbol

def main():
    print("=" * 70)
    print("COMPARACIÓN: Secuencial vs Binaria vs Árbol BST")
    print("=" * 70)
    print(f"{'Tamaño':<10} {'Secuencial (s)':<18} {'Binaria (s)':<16} {'Árbol BST (s)':<16}")
    print("-" * 70)

    for n in [100, 1000, 5000, 10000, 50000]:
        sec, bin_, arb = medir_tiempos(n)
        print(f"{n:<10} {sec:<18.8f} {bin_:<16.8f} {arb:<16.8f}")

    print("-" * 70)
    print("\n📋 Copiar estos tiempos a docs/07-analisis-tp3.md")

if __name__ == "__main__":
    main()
