'''
Los métodos "buscar_solucion_UCS()" y "buscar_solucion_BFS()" fueron tomados del libro:
INTELIGENCIA ARTIFICIAL, Fundamentos, práctica y aplicaciones.
Alberto García Serrano, 2012, pag 43 y pag 61. 
'''
from arbol import Nodo
from mapas import *

class Metodo_de_Busqueda(Nodo):
    def __init__(self, mapaElegido, estado_inicial,solucion):
        self.mapaElegido = mapaElegido
        self.estado_inicial = estado_inicial
        self.solucion = solucion  
    # Código para el algoritmo de búsqueda por coste uniforme:
    def buscar_solucion_UCS(self):
        self.solucionado = False
        self.nodos_visitados = []
        self.nodos_frontera = []
        self.nodo_inicial = Nodo(self.estado_inicial)
        self.nodo_inicial.set_coste(0)   
        self.nodos_frontera.append(self.nodo_inicial)

        # Los métodos "compara" y "comp_to_key" lo único que hacen es indicarle al método "sorted" cómo ordenar los elementos.
        def compara(x,y):
            return x.get_coste() - y.get_coste()
        def cmp_to_key(mycmp):
            'Convert a cmp= function into a key= function'
            class K:
                def __init__(self, obj, *args):
                    self.obj = obj
                def __lt__(self, other):
                    return mycmp(self.obj, other.obj) < 0
                def __gt__(self, other):
                    return mycmp(self.obj, other.obj) > 0
                def __eq__(self, other):
                    return mycmp(self.obj, other.obj) == 0
                def __le__(self, other):
                    return mycmp(self.obj, other.obj) <= 0
                def __ge__(self, other):
                    return mycmp(self.obj, other.obj) >= 0
                def __ne__(self, other):
                    return mycmp(self.obj, other.obj) != 0
            return K

        while not self.solucionado and len(self.nodos_frontera) != 0:
            #Se ordena la lista de nodos frontera:
            self.nodos_frontera = sorted(self.nodos_frontera, key = cmp_to_key(compara))
            self.nodo=self.nodos_frontera[0]
            #Se extrae el nodo y se añade a los nodos visitados:
            self.nodos_visitados.append(self.nodos_frontera.pop(0))

            if (self.nodo.get_datos()) == self.solucion:
                #Solucion encontrada
                self.solucionado = True
                return self.nodo
            else:
                #Se expanden los nodos hijos (casillas siguientes que se pueden recorrer)
                self.dato_nodo = self.nodo.get_datos()
                self.lista_hijos = []
                for self.un_hijo in self.mapaElegido[self.dato_nodo]:
                    self.hijo = Nodo(self.un_hijo)
                    self.coste = self.mapaElegido[self.dato_nodo][self.un_hijo]
                    self.hijo.set_coste(self.nodo.get_coste() + self.coste)
                    self.lista_hijos.append(self.hijo)

                    if not self.hijo.en_lista(self.nodos_visitados):
                        if self.hijo.en_lista(self.nodos_frontera):
                            for self.n in self.nodos_frontera:
                                if self.n.igual(self.hijo) and self.n.get_coste() > self.hijo.get_coste():
                                    self.nodos_frontera.remove(self.n)
                                    self.nodos_frontera.append(self.hijo)
                        else:
                            self.nodos_frontera.append(self.hijo)
                self.nodo.set_hijos(self.lista_hijos)
            
    # Código para el algoritmo de búsqueda por amplitud:
    def buscar_solucion_BFS(self):
        self.solucionado = False
        self.nodos_visitados = []
        self.nodos_frontera = []
        self.nodoInicial = Nodo(self.estado_inicial)
        self.nodos_frontera.append(self.nodoInicial)

        while not self.solucionado and len(self.nodos_frontera) != 0:
            self.nodo = self.nodos_frontera[0]
            #Se extrae el nodo y se añade a visitados
            self.nodos_visitados.append(self.nodos_frontera.pop(0))
            if self.nodo.get_datos() == self.solucion:
                #Solucion encontrada
                self.solucionado = True
                return self.nodo
            else: 
                #expandir nodos hijo (casillas siguientes que se pueden recorrer)
                self.dato_nodo = self.nodo.get_datos()
                self.lista_hijos = []
                for self.un_hijo in self.mapaElegido[self.dato_nodo]:
                    self.hijo = Nodo(self.un_hijo)
                    self.lista_hijos.append(self.hijo)
                    if not self.hijo.en_lista(self.nodos_visitados) and not self.hijo.en_lista(self.nodos_frontera):
                        self.nodos_frontera.append(self.hijo)

            self.nodo.set_hijos(self.lista_hijos)
###########################################################################################################################################################################
# Esta sección del código está para cuando se quiera ejecutar sólo el archivo "ambasBusquedas.py" sin necesidad de ejecutar la interfaz.
# Es posible probar los algoritmos desde una terminal.

if __name__=="__main__":
    mapaEscogido = Mapa.mapa3
    origen = input("Ingrese ciudad origen: " )
    destino = input("Ingrese destino: ")

    tipoDeCalculo = 0
    
    while tipoDeCalculo != '1' and tipoDeCalculo != '2':
        tipoDeCalculo = input("Para calcular la ruta con menos consumo de energía digite 1 , si desea calcular la más corta digite 2 : ")
        if tipoDeCalculo == '1':
            nodo_solucion = Metodo_de_Busqueda(mapaEscogido, origen, destino).buscar_solucion_UCS()
            
        elif tipoDeCalculo == '2':
            nodo_solucion = Metodo_de_Busqueda(mapaEscogido, origen, destino).buscar_solucion_BFS()
            
        else:
            print("No digito ni 1 ni 2, intente nuevamente.") 

    #Mostrar resultado:
    resultado = []
    nodo = nodo_solucion
    while nodo.get_padre() != None:
        resultado.append(nodo.get_datos())
        nodo = nodo.get_padre()  
    resultado.append(origen)
    resultado.reverse()
    print(resultado)
    print("Coste: " + str(nodo_solucion.get_coste())) 

#############################################################################################################################################################################