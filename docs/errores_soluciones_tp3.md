# Errores y Soluciones — TP3: Árbol Binario de Búsqueda
**Proyecto:** GastroRecommender
**Grupo:** 3

## 1. Error al cargar datos desde JSON
- **Qué pasaba:** Al elegir la opción 1, el programa cerraba o aparecía el mensaje *"Error al cargar"*. La ruta al archivo no era correcta y no encontraba el archivo `ingredientes_receta.json`.
- **Causa:** La ruta escrita no coincidía con la ubicación real de la carpeta `datos`.
- **Solución:** Se corrigió la ruta a `datos/ingredientes_receta.json` y se verificó que la estructura de carpetas coincida: `proyecto/datos/archivo.json`.

## 2. Clase `Alimento` no recibía bien los datos
- **Qué pasaba:** Al cargar, aparecía un error sobre argumentos y mapeo en la clase.
- **Causa:** El método `__init__` no tenía los parámetros bien definidos o faltaba inicializar valores por defecto.
- **Solución:** Se corrigió el constructor `def __init__(self, ...)` con todos los atributos y se agregaron valores por defecto para evitar fallos si faltaba algún dato.

## 3. Opción 1 y 2 no mostraban nada / se borraba el menú
- **Qué pasaba:** Escribía `1` o `2`, apretaba Enter y desaparecía todo sin mostrar nada.
- **Causa:** Faltaba que el programa espere correctamente los datos cargados antes de mostrar listas, y había problemas de indentación en el código.
- **Solución:** Se ordenó la lógica del menú, se aseguró que la carga se haga antes de listar y se corrigió la alineación del código (4 espacios por nivel).

## 4. Importaciones no encontraban los archivos
- **Qué pasaba:** Aparecía *"ModuleNotFoundError"* con rutas en rojo.
- **Causa:** Faltaban los archivos `__init__.py` en las carpetas `modelos/` y `servicios/` para que Python las reconozca como paquetes.
- **Solución:** Se crearon los archivos vacíos `__init__.py` en ambas carpetas y se corrigieron las líneas `from ... import ...` con los nombres exactos.

## 5. Confusión con carpetas y archivos al subir a GitHub
- **Qué pasaba:** Se creó una carpeta `TP3_ArbolBinario` separada en lugar de integrar los cambios al código que ya teníamos.
- **Causa:** No se entendía bien que los cambios van sobre lo que ya existe, no en una carpeta nueva aparte.
- **Solución:** Se borró la carpeta separada y se integró el árbol binario dentro de `modelos/`, `servicios/` y `ui/` del proyecto principal.

## 6. Indentación y espacios mal alineados
- **Qué pasaba:** Líneas en rojo, errores raros que no se entendían.
- **Causa:** Python es estricto con los espacios; si no están alineados igual, no funciona.
- **Solución:** Se usaron siempre 4 espacios por nivel, se revisó línea por línea y se reescribió el código completo donde era necesario.
