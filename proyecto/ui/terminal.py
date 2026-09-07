# ui/terminal.py

import json
import os
import sys
from datetime import datetime, timedelta

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from modelos.ingredientes_y_recetas import Alimento, Receta


def cargar_datos(): # Carga archivo .json

    try:
        with open("datos/ingredientes_recetas.json", "r", encoding="utf-8") as f:
            data = json.load(f)
        
        ingredientes = []
        for d in data.get("ingredientes", []):
            ingredientes.append(Alimento(
                d["nombre"],
                d["categoria"],
                d["vencimiento"],
                d["cantidad"]
            ))
        
        recetas = []
        for d in data.get("recetas", []):
            recetas.append(Receta(
                d["nombre"],
                d["ingredientes"],
                d["tiempo"],
                d["objetivo"],
                d["dificultad"]
            ))
        
        return ingredientes, recetas
    
    except FileNotFoundError:
        print("Error: Archivo 'datos/ingredientes_recetas.json' no encontrado")
        return [], []
    except json.JSONDecodeError:
        print("Error: El archivo JSON tiene formato inválido")
        return [], []


def guardar_datos(ingredientes, recetas): # Guarda los datos en .json
    
    try:
        data = {
            "ingredientes": [
                {
                    "nombre": i.nombre,
                    "categoria": i.categoria,
                    "vencimiento": i.vencimiento,
                    "cantidad": i.cantidad
                }
                for i in ingredientes
            ],
            "recetas": [
                {
                    "nombre": r.nombre,
                    "ingredientes": r.ingredientes,
                    "tiempo": r.tiempo,
                    "objetivo": r.objetivo,
                    "dificultad": r.dificultad
                }
                for r in recetas
            ]
        }
        
        with open("datos/ingredientes_recetas.json", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        
        return True
    except Exception as e:
        print(f"❌ Error al guardar: {e}")
        return False


def mostrar_menu_principal(): # Menu principal
   
    print("\n" + "=" * 50)
    print("   🍳 GASTRORECOMMENDER 🍳")
    print("=" * 50)
    print("1. 📦 Stock de ingredientes")
    print("2. 📋 Lista de recetas")
    print("3. 🎯 Recomendar receta")
    print("4. 🛒 Recordatorio de compra")
    print("5. ⚠️ Ingredientes vencidos o por vencer")
    print("0. 🚪 Salir")
    print("-" * 50)


def mostrar_submenu_stock():
    
    print("\n" + "-" * 40)
    print("   📦 GESTIÓN DE STOCK")
    print("-" * 40)
    print("1. Ver todos los ingredientes")
    print("2. Agregar ingrediente")
    print("3. Quitar ingrediente")
    print("4. Volver al menú principal")
    print("-" * 40)


def mostrar_submenu_recetas():
    
    print("\n" + "-" * 40)
    print("   📋 GESTIÓN DE RECETAS")
    print("-" * 40)
    print("1. Ver todas las recetas")
    print("2. Ver detalle de una receta")
    print("3. Modificar receta")
    print("4. Eliminar receta")
    print("5. Volver al menú principal")
    print("-" * 40)


def ver_ingredientes(ingredientes):
    
    if not ingredientes:
        print("\n❌ No hay ingredientes en el stock.")
        return
    
    print("\n📦 LISTA DE INGREDIENTES:")
    print("-" * 40)
    for i, ing in enumerate(ingredientes, 1):
        print(f"{i}. {ing}")


def agregar_ingrediente(ingredientes):
    """Agrega un nuevo ingrediente"""
    print("\n➕ AGREGAR INGREDIENTE")
    nombre = input("Nombre: ").strip()
    if not nombre:
        print("❌ El nombre no puede estar vacío.")
        return
    
    # Verificar si ya existe
    for ing in ingredientes:
        if ing.nombre.lower() == nombre.lower():
            print(f"❌ El ingrediente '{nombre}' ya existe.")
            return
    
    categoria = input("Categoría (Carnes, Verduras, Granos, Lácteos, Aceites, Condimentos, Pastas): ").strip()
    vencimiento = input("Fecha de vencimiento (YYYY-MM-DD): ").strip()
    try:
        cantidad = float(input("Cantidad: ").strip())
        if cantidad < 0:
            print("❌ La cantidad no puede ser negativa.")
            return
    except ValueError:
        print("❌ Cantidad inválida.")
        return
    
    ingredientes.append(Alimento(nombre, categoria, vencimiento, cantidad))
    if guardar_datos(ingredientes, []):  # Solo guardamos ingredientes
        print(f"✅ Ingrediente '{nombre}' agregado correctamente.")


def quitar_ingrediente(ingredientes):
    """Quita un ingrediente del stock"""
    if not ingredientes:
        print("\n❌ No hay ingredientes para quitar.")
        return
    
    ver_ingredientes(ingredientes)
    try:
        idx = int(input("\nNúmero del ingrediente a quitar (0 para cancelar): "))
        if idx == 0:
            return
        if 1 <= idx <= len(ingredientes):
            eliminado = ingredientes.pop(idx - 1)
            if guardar_datos(ingredientes, []):
                print(f"✅ Ingrediente '{eliminado.nombre}' eliminado correctamente.")
        else:
            print("❌ Número inválido.")
    except ValueError:
        print("❌ Entrada inválida.")


def ver_recetas(recetas):
    """Muestra todas las recetas"""
    if not recetas:
        print("\n❌ No hay recetas disponibles.")
        return
    
    print("\n📋 LISTA DE RECETAS:")
    print("-" * 40)
    for i, receta in enumerate(recetas, 1):
        print(f"{i}. {receta.nombre} - {receta.objetivo} ({receta.dificultad}) ⏱️{receta.tiempo}min")


def ver_detalle_receta(recetas):
    """Muestra el detalle completo de una receta"""
    if not recetas:
        print("\n❌ No hay recetas disponibles.")
        return
    
    ver_recetas(recetas)
    try:
        idx = int(input("\nNúmero de la receta (0 para cancelar): "))
        if idx == 0:
            return
        if 1 <= idx <= len(recetas):
            receta = recetas[idx - 1]
            print("\n" + "=" * 40)
            print(f"📋 {receta.nombre}")
            print("=" * 40)
            print(f"🎯 Objetivo: {receta.objetivo}")
            print(f"⏱️ Tiempo: {receta.tiempo} minutos")
            print(f"📊 Dificultad: {receta.dificultad}")
            print(f"🍽️ Ingredientes:")
            for ing in receta.ingredientes:
                print(f"   - {ing}")
            print("=" * 40)
        else:
            print("❌ Número inválido.")
    except ValueError:
        print("❌ Entrada inválida.")


def modificar_receta(recetas):
    """Modifica una receta existente"""
    if not recetas:
        print("\n❌ No hay recetas para modificar.")
        return
    
    ver_recetas(recetas)
    try:
        idx = int(input("\nNúmero de la receta a modificar (0 para cancelar): "))
        if idx == 0:
            return
        if 1 <= idx <= len(recetas):
            receta = recetas[idx - 1]
            print(f"\n✏️ Modificando: {receta.nombre}")
            print("(Presiona Enter para mantener el valor actual)")
            
            nuevo_nombre = input(f"Nuevo nombre [{receta.nombre}]: ").strip()
            if nuevo_nombre:
                receta._nombre = nuevo_nombre
            
            nuevos_ingredientes = input(f"Nuevos ingredientes (separados por coma) [{', '.join(receta.ingredientes)}]: ").strip()
            if nuevos_ingredientes:
                receta._ingredientes = [i.strip() for i in nuevos_ingredientes.split(',')]
            
            nuevo_tiempo = input(f"Nuevo tiempo [{receta.tiempo}]: ").strip()
            if nuevo_tiempo:
                try:
                    receta._tiempo = int(nuevo_tiempo)
                except ValueError:
                    print("❌ Tiempo inválido, se mantiene el valor actual.")
            
            nuevo_objetivo = input(f"Nuevo objetivo [{receta.objetivo}]: ").strip()
            if nuevo_objetivo:
                receta._objetivo = nuevo_objetivo
            
            nueva_dificultad = input(f"Nueva dificultad [{receta.dificultad}]: ").strip()
            if nueva_dificultad:
                receta._dificultad = nueva_dificultad
            
            if guardar_datos([], recetas):
                print("✅ Receta modificada correctamente.")
        else:
            print("❌ Número inválido.")
    except ValueError:
        print("❌ Entrada inválida.")


def eliminar_receta(recetas):
    """Elimina una receta"""
    if not recetas:
        print("\n❌ No hay recetas para eliminar.")
        return
    
    ver_recetas(recetas)
    try:
        idx = int(input("\nNúmero de la receta a eliminar (0 para cancelar): "))
        if idx == 0:
            return
        if 1 <= idx <= len(recetas):
            eliminada = recetas.pop(idx - 1)
            if guardar_datos([], recetas):
                print(f"✅ Receta '{eliminada.nombre}' eliminada correctamente.")
        else:
            print("❌ Número inválido.")
    except ValueError:
        print("❌ Entrada inválida.")


def recomendar_receta(recetas):
    """Recomienda una receta según el objetivo del usuario"""
    if not recetas:
        print("\n❌ No hay recetas disponibles.")
        return
    
    print("\n🎯 RECOMENDACIÓN DE RECETAS")
    print("-" * 40)
    print("Objetivos disponibles:")
    
    objetivos = sorted(set(r.objetivo for r in recetas))
    for i, obj in enumerate(objetivos, 1):
        print(f"{i}. {obj}")
    
    try:
        opcion = int(input("\nElige un objetivo (0 para cancelar): "))
        if opcion == 0:
            return
        if 1 <= opcion <= len(objetivos):
            objetivo_elegido = objetivos[opcion - 1]
            recetas_filtradas = [r for r in recetas if r.objetivo == objetivo_elegido]
            
            print(f"\n🍳 Recetas para '{objetivo_elegido}':")
            print("-" * 40)
            for i, receta in enumerate(recetas_filtradas, 1):
                print(f"{i}. {receta.nombre} ({receta.dificultad}) ⏱️{receta.tiempo}min")
        else:
            print("❌ Opción inválida.")
    except ValueError:
        print("❌ Entrada inválida.")


def recordatorio_compra(ingredientes):
    """Muestra ingredientes con cantidad 0 o muy baja"""
    if not ingredientes:
        print("\n❌ No hay ingredientes en el stock.")
        return
    
    print("\n🛒 RECORDATORIO DE COMPRA")
    print("-" * 40)
    
    encontrados = False
    for ing in ingredientes:
        if ing.cantidad <= 0:
            print(f"⚠️ {ing.nombre} - ¡AGOTADO!")
            encontrados = True
        elif ing.cantidad <= 5:
            print(f"⚠️ {ing.nombre} - Cantidad baja: {ing.cantidad}")
            encontrados = True
    
    if not encontrados:
        print("✅ Todos los ingredientes tienen stock suficiente.")


def ingredientes_vencidos(ingredientes):
    """Muestra ingredientes vencidos o por vencer"""
    if not ingredientes:
        print("\n❌ No hay ingredientes en el stock.")
        return
    
    hoy = datetime.now().date()
    print("\n⚠️ INGREDIENTES VENCIDOS O POR VENCER")
    print("-" * 40)
    
    vencidos = []
    por_vencer = []
    otros = []
    
    for ing in ingredientes:
        try:
            fecha_venc = datetime.strptime(ing.vencimiento, "%Y-%m-%d").date()
            dias = (fecha_venc - hoy).days
            
            if dias < 0:
                vencidos.append((ing, dias))
            elif dias <= 7:
                por_vencer.append((ing, dias))
            else:
                otros.append((ing, dias))
        except ValueError:
            print(f"⚠️ {ing.nombre}: Fecha inválida '{ing.vencimiento}'")
    
    # Mostrar vencidos
    if vencidos:
        print("\n🔴 VENCIDOS:")
        for ing, dias in sorted(vencidos, key=lambda x: x[1]):
            print(f"   ❌ {ing.nombre} - Vencido hace {abs(dias)} días")
    
    # Mostrar por vencer
    if por_vencer:
        print("\n🟡 POR VENCER (7 días o menos):")
        for ing, dias in sorted(por_vencer, key=lambda x: x[1]):
            print(f"   ⚠️ {ing.nombre} - Vence en {dias} días")
    
    # Mostrar en buen estado
    if otros:
        print("\n✅ EN BUEN ESTADO:")
        for ing, dias in sorted(otros, key=lambda x: x[1]):
            print(f"   ✅ {ing.nombre} - Vence en {dias} días")
    
    if not vencidos and not por_vencer and not otros:
        print("✅ No hay ingredientes registrados.")


def main():
    """Función principal del programa"""
    # Cargar datos
    ingredientes, recetas = cargar_datos()
    
    if not ingredientes and not recetas:
        print("⚠️ No se pudieron cargar los datos. Verifica el archivo JSON.")
        return
    
    print("\n✅ Datos cargados correctamente!")
    print(f"   📦 {len(ingredientes)} ingredientes")
    print(f"   🍳 {len(recetas)} recetas")
    
    while True:
        mostrar_menu_principal()
        opcion = input("\nElige una opción: ").strip()
        
        if opcion == "1":
            # Submenú de stock
            while True:
                mostrar_submenu_stock()
                sub_opcion = input("Elige una opción: ").strip()
                
                if sub_opcion == "1":
                    ver_ingredientes(ingredientes)
                elif sub_opcion == "2":
                    agregar_ingrediente(ingredientes)
                elif sub_opcion == "3":
                    quitar_ingrediente(ingredientes)
                elif sub_opcion == "4":
                    break
                else:
                    print("❌ Opción inválida. Intenta de nuevo.")
        
        elif opcion == "2":
            # Submenú de recetas
            while True:
                mostrar_submenu_recetas()
                sub_opcion = input("Elige una opción: ").strip()
                
                if sub_opcion == "1":
                    ver_recetas(recetas)
                elif sub_opcion == "2":
                    ver_detalle_receta(recetas)
                elif sub_opcion == "3":
                    modificar_receta(recetas)
                elif sub_opcion == "4":
                    eliminar_receta(recetas)
                elif sub_opcion == "5":
                    break
                else:
                    print("❌ Opción inválida. Intenta de nuevo.")
        
        elif opcion == "3":
            recomendar_receta(recetas)
        
        elif opcion == "4":
            recordatorio_compra(ingredientes)
        
        elif opcion == "5":
            ingredientes_vencidos(ingredientes)
        
        elif opcion == "0":
            print("\n👋 ¡Hasta luego! Gracias por usar GastroRecommender.")
            break
        
        else:
            print("❌ Opción inválida. Intenta de nuevo.")
        
        input("\nPresiona Enter para continuar...")


if __name__ == "__main__":
    main()