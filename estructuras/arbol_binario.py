class NodoBST:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

class ArbolBinarioBusqueda:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        if not self.raiz:
            self.raiz = NodoBST(valor)
        else:
            self._insertar_recursivo(self.raiz, valor)

    def _insertar_recursivo(self, nodo, valor):
        if valor < nodo.valor:
            if nodo.izquierda is None:
                nodo.izquierda = NodoBST(valor)
            else:
                self._insertar_recursivo(nodo.izquierda, valor)
        elif valor > nodo.valor:
            if nodo.derecha is None:
                nodo.derecha = NodoBST(valor)
            else:
                self._insertar_recursivo(nodo.derecha, valor)

    def buscar(self, valor):
        return self._buscar_recursivo(self.raiz, valor)

    def _buscar_recursivo(self, nodo, valor):
        if nodo is None:
            return None
        if valor == nodo.valor:
            return nodo.valor
        elif valor < nodo.valor:
            return self._buscar_recursivo(nodo.izquierda, valor)
        else:
            return self._buscar_recursivo(nodo.derecha, valor)

    def inorden(self):
        res = []
        self._inorden_rec(self.raiz, res)
        return res

    def _inorden_rec(self, nodo, lista):
        if nodo:
            self._inorden_rec(nodo.izquierda, lista)
            lista.append(nodo.valor)
            self._inorden_rec(nodo.derecha, lista)

    def preorden(self):
        res = []
        self._preorden_rec(self.raiz, res)
        return res

    def _preorden_rec(self, nodo, lista):
        if nodo:
            lista.append(nodo.valor)
            self._preorden_rec(nodo.izquierda, lista)
            self._preorden_rec(nodo.derecha, lista)

    def postorden(self):
        res = []
        self._postorden_rec(self.raiz, res)
        return res

    def _postorden_rec(self, nodo, lista):
        if nodo:
            self._postorden_rec(nodo.izquierda, lista)
            self._postorden_rec(nodo.derecha, lista)
            lista.append(nodo.valor)
