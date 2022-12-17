import punto_fijo as pf
from math import sin, cos, tan, pi, e
import tkinter
import customtkinter

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

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
        self.geometry("1200x850")

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

        self.punto_fijo_title.grid(row=0, column=0, padx=30, pady=(40,20),columnspan=3)


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
        self.descripcion_error_entry.grid(row=12, column=0, padx=30, pady=(10,0),sticky="w")

        self.error_entry = customtkinter.CTkEntry(master=self.punto_fijo_frame,width=170,height=40,font=customtkinter.CTkFont(size=STRING_SIZE, weight="normal"))
        self.error_entry.grid(row=13, column=0, padx=30, pady=(0,0),sticky="w")

        ##############################

        ## Botón calcular

        self.calcular_button = customtkinter.CTkButton(master=self.punto_fijo_frame, command=self.calcular_punto_fijo, text="Calcular",font=customtkinter.CTkFont(size=STRING_SIZE, weight="normal"),height=40)
        self.calcular_button.grid(row=14, column=0, padx=30, pady=(20,0),sticky="w")

        self.lienzo = customtkinter.CTkCanvas(master=self.punto_fijo_frame)
        self.lienzo.grid(row=2, column=1,rowspan=14)

        # Create second frame
        self.gauss_seidel_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        # Create third frame
        self.biseccion_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        # Select default frame
        self.select_frame_by_name("punto_fijo")

    def evaluar_funcion(self,x):
        return eval (self.funcion_entry.get())

    def calcular_punto_fijo(self):
        f = self.funcion_entry.get()
        ext_i = int(self.ext_i_entry.get())
        ext_d = int(self.ext_d_entry.get())
        x_inicial = self.x_inicial_entry.get()
        iteraciones = self.iteraciones_entry.get()
        error = float(self.error_entry.get())
        
        mensaje, punto = pf.punto_fijo(f,ext_i,ext_d,x_inicial,iteraciones,error)
        
        figura = plt.Figure(figsize=(5,4))
        graph = np.linspace(ext_i,ext_d,1000)
        figura.add_subplot(111).plot(graph,self.evaluar_funcion(graph))
        chart = FigureCanvasTkAgg(figura, self.lienzo)
        chart.get_tk_widget().pack()


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
        if name == "frame_2":
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