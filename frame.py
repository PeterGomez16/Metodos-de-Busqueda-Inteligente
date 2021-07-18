
# Se importan las librerías necesarias
from tkinter import *
from tkinter import ttk, messagebox
from arbol import Nodo
from mapas import Mapa
from ambasBusquedas import Metodo_de_Busqueda


class Mi_Interfaz(Frame):
    def __init__(self, master=None):
        super().__init__(master, width=800, height=600)    
        self.master = master
        self.pack()
        self.config(bg="azure3")
        self.frame_0()
        self.frame_2()
        self.frame_3()
        self.frame_4()
        self.frame_5()
  
#-------------------------------------------------------------------------#      
    def busquedaSolicitada(self, x):
        inicio = self.entrada_origen.get()
        final = self.entrada_destino.get()
        mapa = self.lista_mapas.get()

        if mapa == 'Mapa 1':
            mapaSeleccionado = Mapa.mapa1
        elif mapa == 'Mapa 2':
            mapaSeleccionado = Mapa.mapa2
        elif mapa == 'Mapa 3':
            mapaSeleccionado = Mapa.mapa3
        elif mapa == 'mapaPrueba':
            mapaSeleccionado = Mapa.mapaPrueba
        #Código para los mensajes de error:
        valido1 = False
        valido2 = False
        for clave in mapaSeleccionado:
            if inicio == clave:
                valido1 = True
        for clave in mapaSeleccionado:
            if final == clave:
                valido2 = True
        if valido1 == False:
            messagebox.showwarning(message="Casilla de origen inválida. Intente nuevamente", title="Título")
        if valido2 == False:
            messagebox.showwarning(message="Casilla de destino inválida. Intente nuevamente", title="Título")

        #Código que ejecuta el método de búsqueda seleccionado:
        if x==1:
            nodo_solucion = Metodo_de_Busqueda(mapaSeleccionado, inicio, final).buscar_solucion_BFS()
        elif x==2:
            nodo_solucion = Metodo_de_Busqueda(mapaSeleccionado, inicio, final).buscar_solucion_UCS()

        resultado = []
        nodo = nodo_solucion
        while nodo.get_padre() != None:
            resultado.append(nodo.get_datos())
            nodo = nodo.get_padre()
        resultado.append(inicio)
        resultado.reverse() 
        coste = str(nodo_solucion.get_coste())

        #Código de diferentes cuadros de texto:
        cuadroParaMostrarOrigen = Entry(self.frame4)
        cuadroParaMostrarOrigen.place(x=165, y=5, width=30)
        cuadroParaMostrarOrigen.delete(0, END)
        cuadroParaMostrarOrigen.insert(3, inicio)
        cuadroParaMostrarOrigen.config(state="readonly", relief=FLAT)

        cuadroParaMostrarDestino = Entry(self.frame4)
        cuadroParaMostrarDestino.place(x=215, y=5,  width=30)
        cuadroParaMostrarDestino.delete(0, END)
        cuadroParaMostrarDestino.insert(3, final)
        cuadroParaMostrarDestino.config(state="readonly", relief=FLAT)

        cajaResultado = Text(self.frame4)
        cajaResultado.place(x=10,y=30, width = 530, height=25)
        cajaResultado.delete('1.0', END)
        cajaResultado.insert('1.0', resultado)
        cajaResultado.config(state=DISABLED, relief=FLAT)

        cajaCoste = Text(self.frame5)
        cajaCoste.place(x=10,y=30, width = 100, height=25)
        cajaCoste.delete('1.0', END)
        cajaCoste.insert('1.0', coste)
        cajaCoste.config(state=DISABLED, relief=FLAT)

 #---------------------------FRAME 0---------------------------------------#
 # Este frame es el que está ubicado en la parte superior de la ventana y el que contiene el título.

    def frame_0(self):
        self.frame0 = Frame(self, bg= "white")
        self.frame0.place(x=25, y=65, width=550, height=450)

        self.frameTitle = Frame(self, bg="azure3")
        self.frameTitle.place(x=25, y= 15, width=550, height= 40)

        titulo = Label(self.frameTitle,bg= "azure3" ,text='Algoritmos de búsqueda no informada')
        titulo.pack()
        titulo.config(font=("Verdana",17))

        Label(self.frame0, text="Por medio de esta aplicación, usted podrá explorar los métodos de búsqueda:", bg="white").place(x=10,y=10)
        Label(self.frame0, text=" -Por amplitud", bg="white").place(x=30,y=30)
        Label(self.frame0, text=" -Por coste uniforme", bg="white").place(x=30,y=50)

        self.fondo0 = Text(self.frame0, bg = "beige", padx=5, pady=5)
        self.fondo0.place(x=10, y=70, width=530, height=155)
        self.fondo0.insert(INSERT, " Esta aplicación simula el recorrido de un robot dentro de un mapa dividido en \n casillas.  Cada casilla recorrida implica un consumo de energía del robot, en \n donde, dependiendo del tipo de terreno, se tendrá mayor o menor consumo. \n Por medio de los algoritmos de búsqueda, es posible calcular la ruta más cor-\n ta entre dos casillas sin importar la energía consumida o calcular la ruta de \n menor consumo de energía sin importar la distancia recorrida.  Cada casilla \n tiene un nombre compuesto por su fila (letra en minúscula) y columna (núme- \n ro). Por ejemplo, la casilla inferior izquierda de cada mapa sería la “a1” ")
        self.fondo0.config(state="disable", font=("Verdana",10))
        
        Label(self.frame0, text="Indicaciones:", font="Verdana 11 bold", bg="white").place(x=20, y=235)
        Label(self.frame0, text="1- Seleccione el mapa que desee recorrer y luego presione el botón “Ver”.", bg="white").place(x=20,y=260)
        Label(self.frame0, text="2- Para calcular una ruta entre dos puntos, elija una casilla ORIGEN y una ca- \n silla  DESTINO, indicándolas en los cuadros de la parte superior derecha.", bg="white").place(x=20,y=280)
        Label(self.frame0, text="3- Seleccione el tipo de búsqueda que desea realizar, presionando alguno de \n los dos	botones de  la parte derecha..", bg="white").place(x=20,y=315)
        Label(self.frame0, text="4- La ruta calculada se mostrará en la parte inferior de la pantalla, indicando \n cada casilla por la que se debe recorrer el mapa. ", bg="white").place(x=20,y=350)
        Label(self.frame0, text="5- Para calcular una nueva ruta, repita los pasos anteriores.", bg="white").place(x=20,y=385)


        boton1 = Button(self.frame0, text="Entendido!", command= self.frame_1)
        boton1.config(bg = "snow3", cursor= "hand2", bd=2)
        boton1.place(x=400, y=410, width=100, height=27)

 #---------------------------FRAME 1---------------------------------------#
 # Este es el frame principal, en donde se muestran las indicaciones iniciales y la imagen del mapa seleccionado.
    def frame_1(self):

        self.entrada_origen.config(state=NORMAL)
        self.entrada_destino.config(state=NORMAL)
        self.boton1.config(state=NORMAL)
        self.boton2.config(state=NORMAL)
        
        self.frame1 = Frame(self, bg="white")
        self.frame1.place(x=25, y=65, width=550, height=450)
        Label(self.frame1, text="Elija un mapa: ", bg="white").place(x=25, y= 415)
        self.opciones = ['Mapa 1', 'Mapa 2', 'Mapa 3', 'mapaPrueba']
        self.lista_mapas = ttk.Combobox(self.frame1, width=15, state="readonly", values= self.opciones)
        self.lista_mapas.place(x= 150, y=415)
        self.lista_mapas.current(0)
      
        self.fondo1 = Label(self.frame1, bg= "white")
        self.fondo1.place(x=15, y=15, width = 520, height= 380)


        #Código que muestra la imagen del mapa seleccionado:
            #Dentro de éste metodo es donde se debe agregar otra condición "elif" cuando se quiera agregar otra imagen de mapa.
        def imagenDeFondo():
            mapa = self.lista_mapas.get()
            if mapa == 'Mapa 1':
                self.imagenSeleccionada = "imagenes/mapa1.png"
            elif mapa == 'Mapa 2':
                self.imagenSeleccionada = "imagenes/mapa2.png"
            elif mapa == 'Mapa 3':
                self.imagenSeleccionada = "imagenes/mapa3.png"
            elif mapa == 'mapaPrueba':
                self.imagenSeleccionada = "imagenes/prueba.png"
                
        
            self.fondo1_image = PhotoImage(file = self.imagenSeleccionada)
            self.fondo1["image"] = self.fondo1_image


        verMapa = Button(self.frame1, text="Ver", command= imagenDeFondo)
        verMapa.config(bg = "snow3", cursor= "hand2", bd=2)
        verMapa.place(x=300, y=410, width=70, height=27)

        verIndicaciones = Button(self.frame1, text= "Indicaciones", command=self.frame_0)
        verIndicaciones.config(bg = "snow3", cursor= "hand2", bd=2)
        verIndicaciones.place(x=400, y=410, width=130, height=27)


#---------------------------------FRAME 2---------------------------------------#
# Este frame es el que está ubicado en la parte superior derecha. Es el que muestra los cuadros donde se ingresan las casillas de origen y destino, además de los botones de búsqueda.
    def frame_2(self):
        self.frame2 = Frame(self, bg = "gainsboro")
        self.frame2.place(x=580, y=65, width=195, height=240)

        Label(self.frame2, text= "Origen: ").place(x= 25, y= 20)
        self.entrada_origen = Entry(self.frame2, width= 7)
        self.entrada_origen.place(x=90, y= 20)
        self.entrada_origen.config(state=DISABLED)
   
        Label(self.frame2, text= "Destino: ").place(x= 25, y= 55) 
        self.entrada_destino= Entry(self.frame2, width= 7)
        self.entrada_destino.place(x=90, y= 50)
        self.entrada_destino.config(state=DISABLED)

        Label(self.frame2, text="Seleccione el tipo de \n búsqueda:").place(x=25, y= 100)
        self.boton1 = Button(self.frame2, text="Amplitud", command= lambda:self.busquedaSolicitada(1))  #para ingresar un metodo con parametros se usa: labda: comand funcion()
        self.boton1.config(bg = "snow3", cursor= "hand2", bd=2, state=DISABLED)
        self.boton1.place(x=10, y=140, width=175, height=30)

        self.boton2 = Button(self.frame2, text="Coste Uniforme", command= lambda:self.busquedaSolicitada(2))  #para ingresar un metodo con parametros se usa: labda: comand funcion()
        self.boton2.config(bg = "snow3", cursor= "hand2", bd=2, state=DISABLED)
        self.boton2.place(x=10, y=180, width=175, height=30)


#---------------------------------FRAME 3---------------------------------------#
#Este frame es el que se encuentra justo debajo del frame anterior. Muestra información sobre los mapas.
    def frame_3(self):
        self.frame3 = Frame(self, bg= "gainsboro")
        self.frame3.place(x=580, y=313, width=195, height=202)

        Label(self.frame3, text= "Coste de energía por \n tipo de terreno: ", font="Verdana 9 bold").place(x=25, y=5)   

        self.zona0 = Label(self.frame3, bg= "white")
        self.zona0.place(x=15,y=48, width=32, height=32) 
        self.zona0_imagen = PhotoImage(file= "imagenes/zona0.png")
        self.zona0["image"] = self.zona0_imagen  
        Label(self.frame3, text= "--> Obtáculo \n     (No se recorre)").place(x=50, y=45)

        self.zona1 = Label(self.frame3, bg= "white")
        self.zona1.place(x=15,y=83, width=32, height=32) 
        self.zona1_imagen = PhotoImage(file= "imagenes/zona1.png")
        self.zona1["image"] = self.zona1_imagen
        Label(self.frame3, text= "--> 1").place(x=60, y=90)

        self.zona2 = Label(self.frame3, bg= "white")
        self.zona2.place(x=15,y=118, width=32, height=32) 
        self.zona2_imagen = PhotoImage(file= "imagenes/zona2.png")
        self.zona2["image"] = self.zona2_imagen
        Label(self.frame3, text= "--> 2").place(x=60, y=125)
        
        self.zona3 = Label(self.frame3, bg= "white")
        self.zona3.place(x=15,y=153, width=32, height=32) 
        self.zona3_imagen = PhotoImage(file= "imagenes/zona3.png")
        self.zona3["image"] = self.zona3_imagen
        Label(self.frame3, text= "--> 3").place(x=60, y=160)

#--------------------------------FRAME 4--------------------------------------#
#Este frame está unbicado en la parte inferior izquierda. Es el que muestra el resultado de la ruta calculada.
    def frame_4(self):
        self.frame4 = Frame(self, bg= "gainsboro")
        self.frame4.place(x=25, y=525, width=550, height=65)

        Label(self.frame4, text= "La ruta calculada entre ").place(x=10, y=5)        
        Label(self.frame4, text= "y ").place(x=200, y=5)
        Label(self.frame4, text= "es: ").place(x=245, y=5)

#--------------------------------FRAME 5--------------------------------------#
#Este frame está ubicado en la parte inferior derecha. Es el que muestra el coste de la ruta calculada.
    def frame_5(self):
        self.frame5 = Frame(self, bg= "gainsboro")
        self.frame5.place(x=580, y=525, width=195, height=65)

        Label(self.frame5, text= "Coste: ").place(x=10, y=5)        

