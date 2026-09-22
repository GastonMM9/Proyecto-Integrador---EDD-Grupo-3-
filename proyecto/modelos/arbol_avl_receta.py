from .receta import Receta

class NodoAVL:
    def __init__(self, receta):
        self.receta = receta
        self.izquierda = None
        self.derecha = None
        self.altura = 1

class ArbolAVLRecetas:
    def __init__(self, criterio="nombre"):
        self.raiz = None
        self.criterio = criterio

    def _obtener_valor(self, receta):
        if self.criterio == "nombre":
            return receta.nombre.lower()
        elif self.criterio == "calorias":
            return receta.calorias
        elif self.criterio == "proteinas":
            return receta.proteinas
        return receta.nombre.lower()

    def _altura(self, nodo):
        if not nodo:
            return 0
        return nodo.altura

    def _balance(self, nodo):
        if not nodo:
            return 0
        return self._altura(nodo.izquierda) - self._altura(nodo.derecha)

    def _rotacion_derecha(self, z):
        y = z.izquierda
        T3 = y.derecha
        y.derecha = z
        z.izquierda = T3
        z.altura = 1 + max(self._altura(z.izquierda), self._altura(z.derecha))
        y.altura = 1 + max(self._altura(y.izquierda), self._altura(y.derecha))
        return y

    def _rotacion_izquierda(self, z):
        y = z.derecha
        T2 = y.izquierda
        y.izquierda = z
        z.derecha = T2
        z.altura = 1 + max(self._altura(z.izquierda), self._altura(z.derecha))
        y.altura = 1 + max(self._altura(y.izquierda), self._altura(y.derecha))
        return y

    def insertar(self, receta):
        valor = self._obtener_valor(receta)
        self.raiz = self._insertar_recursivo(self.raiz, valor, receta)

    def _insertar_recursivo(self, nodo, valor, receta):
        if not nodo:
            return NodoAVL(receta)
        if valor < self._obtener_valor(nodo.receta):
            nodo.izquierda = self._insertar_recursivo(nodo.izquierda, valor, receta)
        else:
            nodo.derecha = self._insertar_recursivo(nodo.derecha, valor, receta)

        nodo.altura = 1 + max(self._altura(nodo.izquierda), self._altura(nodo.derecha))
        balance = self._balance(nodo)

        if balance > 1 and valor < self._obtener_valor(nodo.izquierda.receta):
            return self._rotacion_derecha(nodo)
        if balance < -1 and valor > self._obtener_valor(nodo.derecha.receta):
            return self._rotacion_izquierda(nodo)
        if balance > 1 and valor > self._obtener_valor(nodo.izquierda.receta):
            nodo.izquierda = self._rotacion_izquierda(nodo.izquierda)
            return self._rotacion_derecha(nodo)
        if balance < -1 and valor < self._obtener_valor(nodo.derecha.receta):
            nodo.derecha = self._rotacion_derecha(nodo.derecha)
            return self._rotacion_izquierda(nodo)

        return nodo

    def inorden(self):
        resultados = []
        self._inorden_recursivo(self.raiz, resultados)
        return resultados

    def _inorden_recursivo(self, nodo, lista):
        if nodo:
            self._inorden_recursivo(nodo.izquierda, lista)
            lista.append(nodo.receta)
            self._inorden_recursivo(nodo.derecha, lista)

    def altura_total(self):
        return self._altura(self.raiz)
