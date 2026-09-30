class NodoGeneral:
    def __init__(self, dato):
        self.dato = dato
        self.hijos = []

    def __repr__(self):
        return str(self.dato)


class ArbolGeneral:
    def __init__(self):
        self.raiz = None

    def insertar_raiz(self, dato):
        self.raiz = NodoGeneral(dato)
        return self.raiz

    def agregar_hijo(self, nodo_padre, dato):
        if not nodo_padre:
            raise ValueError("El nodo padre no existe")
        nuevo = NodoGeneral(dato)
        nodo_padre.hijos.append(nuevo)
        return nuevo

    def buscar(self, valor):
        if not self.raiz:
            return None
        cola = [self.raiz]
        while cola:
            actual = cola.pop(0)
            if actual.dato == valor:
                return actual
            cola.extend(actual.hijos)
        return None

    def amplitud(self):
        if not self.raiz:
            return []
        res = []
        cola = [self.raiz]
        while cola:
            actual = cola.pop(0)
            res.append(actual.dato)
            cola.extend(actual.hijos)
        return res

    def profundidad_preorder(self, nodo=None, resultado=None):
        if nodo is None:
            nodo = self.raiz
        if resultado is None:
            resultado = []
        if not nodo:
            return resultado
        resultado.append(nodo.dato)
        for hijo in nodo.hijos:
            self.profundidad_preorder(hijo, resultado)
        return resultado
