from .receta import Receta

class NodoArbol:
    def __init__(self, receta):
        self.receta = receta
        self.izquierdo = None
        self.derecho = None

class ArbolBinarioBusqueda:
    def __init__(self, clave_ordenamiento="calorias"):
        self.raiz = None
        self.clave = clave_ordenamiento

    def _obtener_valor(self, receta):
        if self.clave == "calorias":
            return receta.calorias
        elif self.clave == "tiempo":
            return receta.tiempo
        elif self.clave == "proteina":
            return receta.proteina
        else:
            return receta.nombre.lower()

    def insertar(self, receta):
        if not self.raiz:
            self.raiz = NodoArbol(receta)
            return True
        return self._insertar_recursivo(self.raiz, receta)

    def _insertar_recursivo(self, nodo_actual, receta_nueva):
        valor_nuevo = self._obtener_valor(receta_nueva)
        valor_actual = self._obtener_valor(nodo_actual.receta)
        if valor_nuevo < valor_actual:
            if nodo_actual.izquierdo is None:
                nodo_actual.izquierdo = NodoArbol(receta_nueva)
                return True
            return self._insertar_recursivo(nodo_actual.izquierdo, receta_nueva)
        elif valor_nuevo > valor_actual:
            if nodo_actual.derecho is None:
                nodo_actual.derecho = NodoArbol(receta_nueva)
                return True
            return self._insertar_recursivo(nodo_actual.derecho, receta_nueva)
        return False

    def buscar(self, valor_buscar):
        return self._buscar_recursivo(self.raiz, valor_buscar)

    def _buscar_recursivo(self, nodo, valor):
        if nodo is None:
            return None
        valor_actual = self._obtener_valor(nodo.receta)
        if valor == valor_actual:
            return nodo.receta
        elif valor < valor_actual:
            return self._buscar_recursivo(nodo.izquierdo, valor)
        else:
            return self._buscar_recursivo(nodo.derecho, valor)

    def inorden(self):
        res = []
        self._inorden_rec(self.raiz, res)
        return res
    def _inorden_rec(self, n, l):
        if n:
            self._inorden_rec(n.izquierdo, l)
            l.append(n.receta)
            self._inorden_rec(n.derecho, l)

    def preorden(self):
        res = []
        self._pre_rec(self.raiz, res)
        return res
    def _pre_rec(self, n, l):
        if n:
            l.append(n.receta)
            self._pre_rec(n.izquierdo, l)
            self._pre_rec(n.derecho, l)

    def postorden(self):
        res = []
        self._post_rec(self.raiz, res)
        return res
    def _post_rec(self, n, l):
        if n:
            self._post_rec(n.izquierdo, l)
            self._post_rec(n.derecho, l)
            l.append(n.receta)