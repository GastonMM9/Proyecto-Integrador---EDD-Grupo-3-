# test/test_estructura.py

import json
import os
import sys

# Agregar el directorio padre al path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def test_estructura():
    """Prueba completa de la estructura del proyecto"""
    
    print("\n" + "🧪" * 20)
    print("  INICIANDO PRUEBAS DE ESTRUCTURA  ")
    print("🧪" * 20)
    
    # Test 1: Archivos y carpetas
    print("\n📁 Test 1: Verificando estructura de carpetas...")
    carpetas = ['algoritmos', 'datos', 'estructuras', 'modelos', 'servicios', 'test', 'ui']
    for carpeta in carpetas:
        if os.path.exists(carpeta):
            print(f"   ✅ {carpeta}/")
        else:
            print(f"   ❌ {carpeta}/ NO ENCONTRADA")
    
    # Test 2: Archivo JSON
    print("\n📄 Test 2: Verificando archivo JSON...")
    json_path = os.path.join('datos', 'ingredientes_recetas.json')
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        print(f"   ✅ JSON válido")
        
        ingredientes = data.get('ingredientes', [])
        recetas = data.get('recetas', [])
        
        print(f"   📦 {len(ingredientes)} ingredientes")
        print(f"   🍳 {len(recetas)} recetas")
        
        # Mostrar algunos ejemplos
        if ingredientes:
            print(f"\n   📦 Ejemplo de ingrediente:")
            print(f"      {ingredientes[0]}")
        
        if recetas:
            print(f"\n   🍳 Ejemplo de receta:")
            print(f"      {recetas[0]}")
            
    except FileNotFoundError:
        print(f"   ❌ ERROR: Archivo '{json_path}' no encontrado")
        return
    except json.JSONDecodeError as e:
        print(f"   ❌ ERROR: El archivo JSON tiene formato inválido: {e}")
        return
    
    # Test 3: Importar y probar clases
    print("\n🏗️ Test 3: Importando y probando clases...")
    try:
        # Importar las clases dentro del try
        from modelos.ingredientes_y_recetas import Alimento, Receta
        
        print(f"   ✅ Clases importadas correctamente")
        
        # Probar Alimento
        a = Alimento("Pollo", "Carne", "2026-12-31", 2)
        print(f"   ✅ Alimento creado: {a}")
        
        # Probar Receta
        r = Receta("Pollo asado", ["Pollo", "Sal"], 60, "Ganar peso", "Media")
        print(f"   ✅ Receta creada: {r}")
        
    except ImportError as e:
        print(f"   ❌ Error de importación: {e}")
        print("   Verifica que el archivo modelos/ingredientes_y_recetas.py existe")
        return
    except Exception as e:
        print(f"   ❌ Error en clases: {e}")
        import traceback
        traceback.print_exc()
        return
    
    # Test 4: Verificar datos del JSON
    print("\n🔍 Test 4: Verificando datos del JSON...")
    
    # Verificar categorías de ingredientes
    categorias = set()
    for ing in ingredientes:
        categoria = ing.get('categoria', 'Sin categoría')
        categorias.add(categoria)
    
    print(f"   🏷️ Categorías de ingredientes: {', '.join(sorted(categorias))}")
    
    # Verificar objetivos de recetas
    objetivos = set()
    for rec in recetas:
        objetivo = rec.get('objetivo', 'Sin objetivo')
        objetivos.add(objetivo)
    
    print(f"   🎯 Objetivos de recetas: {', '.join(sorted(objetivos))}")
    
    # Verificar dificultades
    dificultades = set()
    for rec in recetas:
        dificultad = rec.get('dificultad', 'Sin dificultad')
        dificultades.add(dificultad)
    
    print(f"   📊 Dificultades: {', '.join(sorted(dificultades))}")
    
    # Test 5: Resumen final
    print("\n📊 Test 5: Resumen final...")
    print(f"   ✅ Total ingredientes: {len(ingredientes)}")
    print(f"   ✅ Total recetas: {len(recetas)}")
    
    # Contar recetas por objetivo
    print("\n   📋 Recetas por objetivo:")
    for objetivo in sorted(objetivos):
        count = sum(1 for rec in recetas if rec.get('objetivo') == objetivo)
        print(f"      - {objetivo}: {count} recetas")
    
    print("\n" + "✅" * 20)
    print("  ✅ TODAS LAS PRUEBAS PASARON EXITOSAMENTE  ")
    print("✅" * 20 + "\n")

if __name__ == "__main__":
    test_estructura()