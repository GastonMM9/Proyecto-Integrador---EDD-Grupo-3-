class NodoArbol:
    def __init__(self, receta):
        self.receta = receta
        self.izquierda = None
        self.derecha = None


class ArbolBinarioBusqueda:
    def __init__(self, criterio="calorias"):
        self.raiz = None
        self.criterio = criterio

    def _obtener_valor(self, receta):
        if self.criterio == "calorias":
            return receta.calorias
        elif self.criterio == "proteina":
            return receta.proteina
        return receta.nombre

    def insertar(self, receta):
        valor = self._obtener_valor(receta)
        nodo_nuevo = NodoArbol(receta)

        if self.raiz is None:
            self.raiz = nodo_nuevo
            return

        actual = self.raiz
        while True:
            valor_actual = self._obtener_valor(actual.receta)
            if valor < valor_actual:
                if actual.izquierda is None:
                    actual.izquierda = nodo_nuevo
                    break
                actual = actual.izquierda
            else:
                if actual.derecha is None:
                    actual.derecha = nodo_nuevo
                    break
                actual = actual.derecha

    def _inorden_recursivo(self, nodo, resultado):
        if nodo:
            self._inorden_recursivo(nodo.izquierda, resultado)
            resultado.append(nodo.receta)
            self._inorden_recursivo(nodo.derecha, resultado)

    def inorden(self):
        resultado = []
        self._inorden_recursivo(self.raiz, resultado)
        return resultado

    def _preorden_recursivo(self, nodo, resultado):
        if nodo:
            resultado.append(nodo.receta)
            self._preorden_recursivo(nodo.izquierda, resultado)
            self._preorden_recursivo(nodo.derecha, resultado)

    def preorden(self):
        resultado = []
        self._preorden_recursivo(self.raiz, resultado)
        return resultado

    def _postorden_recursivo(self, nodo, resultado):
        if nodo:
            self._postorden_recursivo(nodo.izquierda, resultado)
            self._postorden_recursivo(nodo.derecha, resultado)
            resultado.append(nodo.receta)

    def postorden(self):
        resultado = []
        self._postorden_recursivo(self.raiz, resultado)
        return resultado