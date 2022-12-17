import os
import punto_fijo as pf
import gauss_seidel as gs
from sympy import Eq, Interval, Reals, Set, lambdify, symbols, sympify, calculus, plot, sqrt
from sympy import sin, cos, tan, pi, euler as e
import tkinter as tk
import customtkinter

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)))

customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("blue")

TITLE_SIZE = 40
SUBTITLE_SIZE = 23
STRING_SIZE = 18
COLUMN_SPAN = 4


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Proyecto final - Métodos numéricos")
        self.geometry("1220x850")

        # set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)


        ###########################
        # Create navigation frame #
        ###########################

        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(4, weight=1)

        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, text="Métodos \ndisponibles", compound="center", font=customtkinter.CTkFont(size=SUBTITLE_SIZE, weight="bold"))

        self.navigation_frame_label.grid(row=0, column=0, padx=50, pady=(40,30))


        self.punto_fijo_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Punto fijo",font=customtkinter.CTkFont(size=STRING_SIZE, weight="normal"),fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),anchor="w", command=self.punto_fijo_button_event)

        self.punto_fijo_button.grid(row=1, column=0, padx=0, sticky="ew")


        self.gauss_seidel_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Gauss-Seidel",font=customtkinter.CTkFont(size=STRING_SIZE, weight="normal"),fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),anchor="w", command=self.gauss_seidel_button_event)

        self.gauss_seidel_button.grid(row=2, column=0, padx=0, sticky="ew")


        self.biseccion_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Bisección",font=customtkinter.CTkFont(size=STRING_SIZE, weight="normal"),fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"), anchor="w", command=self.biseccion_button_event)

        self.biseccion_button.grid(row=3, column=0, padx=0, sticky="ew")


        ###########################
        # Create punto_fijo frame #
        ###########################

        self.punto_fijo_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        #self.punto_fijo_frame.grid_rowconfigure(0, weight=1)
        #self.punto_fijo_frame.grid_columnconfigure(2, weight=1)

        self.punto_fijo_title = customtkinter.CTkLabel(master=self.punto_fijo_frame, text="Punto Fijo", compound="center", font=customtkinter.CTkFont(size=TITLE_SIZE, weight="bold"))

        self.punto_fijo_title.grid(row=0, column=0, padx=30, pady=(35,15),columnspan=3)


        ##############################

        ## Descripción punto fijo
        
        self.descripcion_punto_fijo = customtkinter.CTkLabel(master=self.punto_fijo_frame, text="Para calcular el punto fijo, se inserta el g(x) de la función despejada 'g(x) = x'. El número de iteraciones y el valor \ninicial son datos opcionales, ya que por defecto las iteraciones calculadas son 100 y el valor inicial se toma como\n el promedio de los extremos del intervalo, dejar en blanco en caso de no trabajar con ellos.",compound="left", font=customtkinter.CTkFont(size=STRING_SIZE, weight="normal"))

        self.descripcion_punto_fijo.grid(row=1, column=0, padx=30, pady=(20, 0),columnspan=3)

        ##############################

        ## Función

        self.descripcion_funcion_entry = customtkinter.CTkLabel(master=self.punto_fijo_frame, text="Ingrese la función en Python*",compound="left", font=customtkinter.CTkFont(size=STRING_SIZE, weight="normal"))
        self.descripcion_funcion_entry.grid(row=2, column=0, padx=30, pady=(40,0),sticky="w")

        self.funcion_entry = customtkinter.CTkEntry(master=self.punto_fijo_frame,width=200,height=40,font=customtkinter.CTkFont(size=STRING_SIZE, weight="normal"))
        self.funcion_entry.grid(row=3, column=0, padx=30, pady=(0,0),sticky="w")

        ##############################

        ## Extremo izquierdo del intervalo

        self.descripcion_ext_i_entry = customtkinter.CTkLabel(master=self.punto_fijo_frame, text="Extremo izquierdo del intervalo*",compound="left", font=customtkinter.CTkFont(size=STRING_SIZE, weight="normal"))
        self.descripcion_ext_i_entry.grid(row=4, column=0, padx=30, pady=(10,0),sticky="w")

        self.ext_i_entry = customtkinter.CTkEntry(master=self.punto_fijo_frame,width=100,height=40,font=customtkinter.CTkFont(size=STRING_SIZE, weight="normal"))
        self.ext_i_entry.grid(row=5, column=0, padx=30, pady=(0,0),sticky="w")

        ##############################

        ## Extremo derecho

        self.descripcion_ext_d_entry = customtkinter.CTkLabel(master=self.punto_fijo_frame, text="Extremo derecho del intervalo*",compound="left", font=customtkinter.CTkFont(size=STRING_SIZE, weight="normal"))
        self.descripcion_ext_d_entry.grid(row=6, column=0, padx=30, pady=(10,0),sticky="w")

        self.ext_d_entry = customtkinter.CTkEntry(master=self.punto_fijo_frame,width=100,height=40,font=customtkinter.CTkFont(size=STRING_SIZE, weight="normal"))
        self.ext_d_entry.grid(row=7, column=0, padx=30, pady=(0,0),sticky="w")

        ##############################

        ## Valor inicial

        self.descripcion_x_inicial_entry = customtkinter.CTkLabel(master=self.punto_fijo_frame, text="Valor inicial",compound="left", font=customtkinter.CTkFont(size=STRING_SIZE, weight="normal"))
        self.descripcion_x_inicial_entry.grid(row=8, column=0, padx=30, pady=(10,0),sticky="w")

        self.x_inicial_entry = customtkinter.CTkEntry(master=self.punto_fijo_frame,width=150,height=40,font=customtkinter.CTkFont(size=STRING_SIZE, weight="normal"))
        self.x_inicial_entry.grid(row=9, column=0, padx=30, pady=(0,0),sticky="w")

        ##############################

        ## Número de iteraciones

        self.descripcion_iteraciones_entry = customtkinter.CTkLabel(master=self.punto_fijo_frame, text="Número de iteraciones",compound="center", font=customtkinter.CTkFont(size=STRING_SIZE, weight="normal"))
        self.descripcion_iteraciones_entry.grid(row=10, column=0, padx=30, pady=(10,0),sticky="w")

        self.iteraciones_entry = customtkinter.CTkEntry(master=self.punto_fijo_frame,width=100,height=40,font=customtkinter.CTkFont(size=STRING_SIZE, weight="normal"))
        self.iteraciones_entry.grid(row=11, column=0, padx=30, pady=(0,0),sticky="w")

        ##############################

        ## Error

        self.descripcion_error_entry = customtkinter.CTkLabel(master=self.punto_fijo_frame, text="Cota de error*",compound="center", font=customtkinter.CTkFont(size=STRING_SIZE, weight="normal"))
        self.descripcion_error_entry.grid(row=12, column=0, padx=30, pady=(0,0),sticky="ws")

        self.error_entry = customtkinter.CTkEntry(master=self.punto_fijo_frame,width=170,height=40,font=customtkinter.CTkFont(size=STRING_SIZE, weight="normal"))
        self.error_entry.grid(row=13, column=0, padx=30, pady=(0,0),sticky="wn")

        ##############################

        ## Botón calcular

        self.calcular_button = customtkinter.CTkButton(master=self.punto_fijo_frame, command=self.calcular_punto_fijo, text="Calcular",font=customtkinter.CTkFont(size=STRING_SIZE, weight="normal"),height=40)
        self.calcular_button.grid(row=14, column=0, padx=30, pady=(20,0),sticky="w")

        # Cargar imagen
        self.imagen_grafica = tk.PhotoImage(file=f"{image_path}/output.png")

        self.grafica_punto_fijo = customtkinter.CTkLabel(master=self.punto_fijo_frame,text="",compound="left",width=400,height=400)
        self.grafica_punto_fijo.grid(row=2,column=1,padx=0,pady=(40,0),sticky="ew",rowspan=10)

        # Caja de texto para logs

        self.punto_fijo_logs = customtkinter.CTkTextbox(master=self.punto_fijo_frame,font=("Calibri",16))
        self.punto_fijo_logs.grid(row=12,column=1,padx=0,pady=(10,10),sticky="ew",rowspan=3)



        ###############
        # GAUS SEIDEL *************************************************************
        ###############

        self.gauss_seidel_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        #Titulo
        self.gauss_seidel_tittle = customtkinter.CTkLabel(master=self.gauss_seidel_frame, text="Gauss-Seidel", compound="center", font=customtkinter.CTkFont(size=TITLE_SIZE, weight="bold"))

        self.gauss_seidel_tittle.grid(row=0, column=3, padx=30, pady=(40,20))
        
        #Matriz
        self.matriz_subtittle = customtkinter.CTkLabel(master=self.gauss_seidel_frame, text="Matriz", compound="center", font=customtkinter.CTkFont(size=SUBTITLE_SIZE, weight="normal"))
         
        self.matriz_subtittle.grid(row=1, column=0, padx=30, pady=(40,20),columnspan=3)

        #Vector
        self.vector_subtittle = customtkinter.CTkLabel(master=self.gauss_seidel_frame, text="Vector S", compound="center", font=customtkinter.CTkFont(size=SUBTITLE_SIZE, weight="normal"))
         
        self.vector_subtittle.grid(row=1, column=3, padx=30, pady=(40,20))

        #Terminos independientes
        self.independientes_subtittle = customtkinter.CTkLabel(master=self.gauss_seidel_frame, text="Terminos \nindependientes", compound="center", font=customtkinter.CTkFont(size=SUBTITLE_SIZE, weight="normal"))
         
        self.independientes_subtittle.grid(row=1, column=4, padx=30, pady=(20,20))

        #Entrys matriz
            ##fila 1
        self.a11_entry = customtkinter.CTkEntry(master=self.gauss_seidel_frame,width=35,height=35,font=customtkinter.CTkFont(size=STRING_SIZE, weight="normal"))
        self.a11_entry.grid(row=2, column=0, padx=10, pady=10)

        self.a12_entry = customtkinter.CTkEntry(master=self.gauss_seidel_frame,width=35,height=35,font=customtkinter.CTkFont(size=STRING_SIZE, weight="normal"))
        self.a12_entry.grid(row=2, column=1, padx=10, pady=10)

        self.a13_entry = customtkinter.CTkEntry(master=self.gauss_seidel_frame,width=35,height=35,font=customtkinter.CTkFont(size=STRING_SIZE, weight="normal"))
        self.a13_entry.grid(row=2, column=2, padx=10, pady=10)

            ##fila 2
        self.a21_entry = customtkinter.CTkEntry(master=self.gauss_seidel_frame,width=35,height=35,font=customtkinter.CTkFont(size=STRING_SIZE, weight="normal"))
        self.a21_entry.grid(row=3, column=0, padx=10, pady=10)

        self.a22_entry = customtkinter.CTkEntry(master=self.gauss_seidel_frame,width=35,height=35,font=customtkinter.CTkFont(size=STRING_SIZE, weight="normal"))
        self.a22_entry.grid(row=3, column=1, padx=10, pady=10)

        self.a23_entry = customtkinter.CTkEntry(master=self.gauss_seidel_frame,width=35,height=35,font=customtkinter.CTkFont(size=STRING_SIZE, weight="normal"))
        self.a23_entry.grid(row=3, column=2, padx=10, pady=10)


            ##fila 3
        self.a31_entry = customtkinter.CTkEntry(master=self.gauss_seidel_frame,width=35,height=35,font=customtkinter.CTkFont(size=STRING_SIZE, weight="normal"))
        self.a31_entry.grid(row=4, column=0, padx=10, pady=10)

        self.a32_entry = customtkinter.CTkEntry(master=self.gauss_seidel_frame,width=35,height=35,font=customtkinter.CTkFont(size=STRING_SIZE, weight="normal"))
        self.a32_entry.grid(row=4, column=1, padx=10, pady=10)

        self.a33_entry = customtkinter.CTkEntry(master=self.gauss_seidel_frame,width=35,height=35,font=customtkinter.CTkFont(size=STRING_SIZE, weight="normal"))
        self.a33_entry.grid(row=4, column=2, padx=10, pady=10)

        #Entrys vector
        self.v1_entry = customtkinter.CTkEntry(master=self.gauss_seidel_frame,width=35,height=35,font=customtkinter.CTkFont(size=STRING_SIZE, weight="normal"))
        self.v1_entry.grid(row=2, column=3, padx=10, pady=10)

        self.v2_entry = customtkinter.CTkEntry(master=self.gauss_seidel_frame,width=35,height=35,font=customtkinter.CTkFont(size=STRING_SIZE, weight="normal"))
        self.v2_entry.grid(row=3, column=3, padx=10, pady=10)

        self.v3_entry = customtkinter.CTkEntry(master=self.gauss_seidel_frame,width=35,height=35,font=customtkinter.CTkFont(size=STRING_SIZE, weight="normal"))
        self.v3_entry.grid(row=4, column=3, padx=10, pady=10)

        #Entrys terminos independientes
        self.t1_entry = customtkinter.CTkEntry(master=self.gauss_seidel_frame,width=35,height=35,font=customtkinter.CTkFont(size=STRING_SIZE, weight="normal"))
        self.t1_entry.grid(row=2, column=4, padx=10, pady=10)

        self.t2_entry = customtkinter.CTkEntry(master=self.gauss_seidel_frame,width=35,height=35,font=customtkinter.CTkFont(size=STRING_SIZE, weight="normal"))
        self.t2_entry.grid(row=3, column=4, padx=10, pady=10)

        self.t3_entry = customtkinter.CTkEntry(master=self.gauss_seidel_frame,width=35,height=35,font=customtkinter.CTkFont(size=STRING_SIZE, weight="normal"))
        self.t3_entry.grid(row=4, column=4, padx=10, pady=10)

        #Text box
        self.box_solucion = customtkinter.CTkTextbox(master=self.gauss_seidel_frame, width=300, height=200, state="disabled",font=("Calibri",16))
        self.box_solucion.grid(row=5, column=0, padx=10, pady=20, columnspan=3,sticky="ew")

        #Entry tolerancia
        self.tolerancia_entry = customtkinter.CTkEntry(master=self.gauss_seidel_frame,width=100, height=30,font=customtkinter.CTkFont(size=12, weight="normal"), placeholder_text="Tolerancia")
        self.tolerancia_entry.grid(row=5, column=4, padx=10, pady=20)

        #Combo box
        self.combo_esquema = customtkinter.CTkComboBox(master=self.gauss_seidel_frame, width=100, height=30,hover=True,values=["3x3","2x2"],command=self.fun_cbox_gs, justify="center")
        self.combo_esquema.grid(row=5, column=3, padx=10, pady=20)

        #Boton calcular
        self.gs_boton_calcular = customtkinter.CTkButton(master=self.gauss_seidel_frame,width=100,height=30,text="Calcular",command=self.fun_calBoton_gs)

        self.gs_boton_calcular.grid(row=5, column=5,padx=10,pady=20)


        #**************************************************************************

        # Create third frame
        self.biseccion_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        # Select default frame
        self.select_frame_by_name("punto_fijo")

    def calcular_punto_fijo(self):
        f = self.funcion_entry.get()
        ext_i = self.ext_i_entry.get()
        ext_d = self.ext_d_entry.get()
        x_inicial = self.x_inicial_entry.get()
        iteraciones = self.iteraciones_entry.get()
        error = float(self.error_entry.get())
        
        logs, punto = pf.punto_fijo(f,ext_i,ext_d,x_inicial,iteraciones,error)

        self.punto_fijo_logs.configure(state="normal")
        self.punto_fijo_logs.delete("1.0","end")

        if type(punto) != str:
            x = pf.symbols('x')
            fun = pf.lambdify(x,f)
            grafico = pf.plot(x,sympify(x,f),(x,float(ext_i),float(ext_d)),show=False,size=(5,4),markers=[{'args': [punto, fun(punto), 'go']}])
            grafico.save("output.png")
            self.grafica_punto_fijo.configure(image=tk.PhotoImage(file=f"{image_path}/output.png"))
        else:
            self.grafica_punto_fijo.configure(image=None)

        for i in range(len(logs)):
            self.punto_fijo_logs.insert(f"{i+1}.0",logs[i])
            self.punto_fijo_logs.insert(tk.END,"\n")
            print(logs[i])
        self.punto_fijo_logs.configure(state="disabled")


    #***Funcion combo box gauss-seidel
    def fun_cbox_gs(self,choice):

        if choice == "2x2":
            gs.funcion = 1
            self.a13_entry.configure(state="disabled")
            self.a23_entry.configure(state="disabled")
            self.a33_entry.configure(state="disabled")
            self.a32_entry.configure(state="disabled")
            self.a31_entry.configure(state="disabled")
            self.v3_entry.configure(state="disabled")
            self.t3_entry.configure(state="disabled")

        elif choice == "3x3":
            gs.funcion = 0
            self.a13_entry.configure(state="normal")
            self.a23_entry.configure(state="normal")
            self.a33_entry.configure(state="normal")
            self.a32_entry.configure(state="normal")
            self.a31_entry.configure(state="normal")
            self.v3_entry.configure(state="normal")
            self.t3_entry.configure(state="normal")

        print(choice)


    #***Funcion de boton calcular gauss-seidel
    def fun_calBoton_gs (self):

        if self.a11_entry.get() != "0" and self.a22_entry.get() != "0" and self.a33_entry.get() != "0":

            if gs.funcion == 0:
                if self.a11_entry.get() != "" and self.a12_entry.get() != "" and self.a13_entry.get() != "" and self.a21_entry.get() != "" and self.a22_entry.get() != "" and self.a23_entry.get() != "" and self.a31_entry.get() != "" and self.a32_entry.get() != "" and self.a33_entry.get() != "":
                    gs.a11 = float(self.a11_entry.get())
                    gs.a12 = float(self.a12_entry.get())
                    gs.a13 = float(self.a13_entry.get())
                    gs.a21 = float(self.a21_entry.get())
                    gs.a22 = float(self.a22_entry.get())
                    gs.a23 = float(self.a23_entry.get())
                    gs.a31 = float(self.a31_entry.get())
                    gs.a32 = float(self.a32_entry.get())
                    gs.a33 = float(self.a33_entry.get())

                    if self.tolerancia_entry.get() != "" and float(self.tolerancia_entry.get()) > 0:
                        gs.tolerancia = float(self.tolerancia_entry.get())

                    else:
                        gs.tolerancia = 0.0001

                    gs.x1 = float(self.v1_entry.get())
                    gs.x2 = float(self.v2_entry.get())
                    gs.x3 = float(self.v3_entry.get())

                    gs.b1 = float(self.t1_entry.get())
                    gs.b2 = float(self.t2_entry.get())
                    gs.b3 = float(self.t3_entry.get())

                    if gs.FunDiagDom3x3 :
                        gs.gauss_seidel()
                        print(gs.vectorS)

                        self.box_solucion.configure(state="normal")
                        self.box_solucion.insert("0.0",text=f"x1 = {gs.x1}\nx2 = {gs.x2}\nx3 = {gs.x3}")
                        self.box_solucion.configure(state="disabled")
                        

                    else:
                        print("La matriz debe ser diagonalmente dominante")
                        self.box_solucion.configure(state="normal")
                        self.box_solucion.insert("0.0",text="La matriz debe ser diagonalmente dominante")
                        self.box_solucion.configure(state="disabled")

                else:
                    print("Debe llenar todos los campos de la matriz")


            else:
                pass


    def select_frame_by_name(self, name):
        # set button color for selected button
        self.punto_fijo_button.configure(fg_color=("gray75", "gray25") if name == "punto_fijo" else "transparent")
        self.gauss_seidel_button.configure(fg_color=("gray75", "gray25") if name == "gauss_seidel" else "transparent")
        self.biseccion_button.configure(fg_color=("gray75", "gray25") if name == "biseccion" else "transparent")

        # show selected frame
        if name == "punto_fijo":
            self.punto_fijo_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.punto_fijo_frame.grid_forget()
        if name == "gauss_seidel":
            self.gauss_seidel_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.gauss_seidel_frame.grid_forget()
        if name == "biseccion":
            self.biseccion_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.biseccion_frame.grid_forget()

    def punto_fijo_button_event(self):
        self.select_frame_by_name("punto_fijo")

    def gauss_seidel_button_event(self):
        self.select_frame_by_name("gauss_seidel")

    def biseccion_button_event(self):
        self.select_frame_by_name("biseccion")

    def change_appearance_mode_event(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)


if __name__ == "__main__":
    app = App()
    app.mainloop()