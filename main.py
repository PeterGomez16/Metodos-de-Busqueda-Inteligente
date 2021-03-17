from arbol import Nodo
from ambasBusquedas import Metodo_de_Busqueda
from mapas import Mapa
from tkinter import *
from tkinter import ttk
from frame import Mi_Interfaz
import os, sys


def main():  #Ejecuta la interfaz grafica
    ventana = Tk()
    ventana.resizable(0,0) #Para que la ventana no sea de tamaño editable
    ventana.title("Métodos de Búsqueda Inteligente")
    app = Mi_Interfaz(ventana)
    app.mainloop() 

if __name__=="__main__":
    main()