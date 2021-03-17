'''
Este código está tomado del libro:
INTELIGENCIA ARTIFICIAL, Fundamentos, práctica y aplicaciones.
Alberto García Serrano, 2012, pag 35. 
'''

class Nodo:
    def __init__(self, datos, hijos=None):
        self.datos = datos
        self.hijos = None
        self.padre = None
        self.coste = None
        self.set_hijos(hijos)

    def set_hijos(self, hijos):         #Asigna al nodo la lista de hijos que son pasados como parámetro
        self.hijos = hijos
        if self.hijos != None:
            for h in self.hijos:
                h.padre = self

    def get_hijos(self):            #Retorna una lista con los hijos del nodo
        return self.hijos

    def get_padre(self):            #Retorna el nodo padre
        return self.padre

    def set_padre(self, padre):     #Asigna el nodo padre de este nodo
        self.padre = padre

    def set_datos(self, datos):      #Asigna un dato al nodo
        self.datos = datos

    def get_datos(self):     #Devuelve el dato almacenado al nodo
        return self.datos

    def set_coste(self, coste):     #Asigna un peso o coste al nodo dentro del árbol
        self.coste = coste

    def get_coste(self):            #Devuelve el peso o coste del nodo dentro del árbol
        return self.coste
    
    def igual(self, nodo):          #Devuelve True si el dato contenido en el nodo es igual al nodo pasado como parámetro
        if self.get_datos() == nodo.get_datos():
            return True
        else:
            return False

    def en_lista(self, lista_nodos):    #Devuelve True si el dato contenido en el nodo es igual a alguno de los nodos contenidos en la lista de nodos pasada como parámetros
        en_la_lista = False
        for n in lista_nodos:
            if self.igual(n):
                en_la_lista = True
        return en_la_lista

    def __str__(self):
        return str(self.get_datos())