class NodoArbol:
    def __init__(self, receta):
        self.receta = receta
        self.izquierda = None
        self.derecha = None


class ArbolBinarioBusqueda:
    def __init__(self, criterio="calorias"):
        self.raiz = None
        self.criterio = criterio

    def _valor(self, receta):
        if self.criterio == "calorias":
            return receta.calorias
        elif self.criterio == "proteina":
            return getattr(receta, "proteina", 0)
        elif self.criterio == "tiempo":
            return getattr(receta, "tiempo", 0)
        return receta.calorias

    def insertar(self, receta):
        if not self.raiz:
            self.raiz = NodoArbol(receta)
        else:
            self._insertar_recursivo(self.raiz, receta)

    def _insertar_recursivo(self, nodo, receta):
        valor_receta = self._valor(receta)
        valor_nodo = self._valor(nodo.receta)
        if valor_receta < valor_nodo:
            if nodo.izquierda:
                self._insertar_recursivo(nodo.izquierda, receta)
            else:
                nodo.izquierda = NodoArbol(receta)
        else:
            if nodo.derecha:
                self._insertar_recursivo(nodo.derecha, receta)
            else:
                nodo.derecha = NodoArbol(receta)

    def inorden(self):
        resultado = []
        self._recorrer_inorden(self.raiz, resultado)
        return resultado

    def _recorrer_inorden(self, nodo, lista):
        if nodo:
            self._recorrer_inorden(nodo.izquierda, lista)
            lista.append(nodo.receta)
            self._recorrer_inorden(nodo.derecha, lista)

    def buscar_por_rango(self, minimo, maximo):
        resultado = []
        self._buscar_rango_recursivo(self.raiz, minimo, maximo, resultado)
        return resultado

    def _buscar_rango_recursivo(self, nodo, minimo, maximo, lista):
        if not nodo:
            return
        valor = self._valor(nodo.receta)
        if minimo < valor:
            self._buscar_rango_recursivo(nodo.izquierda, minimo, maximo, lista)
        if minimo <= valor <= maximo:
            lista.append(nodo.receta)
        if maximo > valor:
            self._buscar_rango_recursivo(nodo.derecha, minimo, maximo, lista)
