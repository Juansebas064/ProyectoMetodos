import math
import tkinter.messagebox
import tkinter as tk
import customtkinter
import matplotlib.pyplot as plt
import numpy as np
from tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from math import e,sin,cos,tan, pi

customtkinter.set_appearance_mode("Light")
customtkinter.set_default_color_theme("dark-blue")



class App(customtkinter.CTk):

    def __init__(self):

        super().__init__()


        # configure window
        self.ecuacion = ""
        self.Xa = 0.0
        self.Xb = 0.0
        self.iteraciones = 0
        self.f_c = 999999
        self.lst = []



        self.tolerancia = 0.0
        self.title("Biseccion - biseccion.py")
        self.geometry(f"{1280}x{720}")

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)



        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=250, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=6, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(6, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Bisección",
                                                 font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))


        # main frame
        self.main_frame = customtkinter.CTkFrame(self, width=600, corner_radius=0)
        self.main_frame.grid(row=0, column=1, rowspan=4, sticky="nsew")

        # table internal table frame

        self.table_frame = customtkinter.CTkFrame(self.main_frame, height=400)
        self.table_frame.grid(row=1, column=4, sticky="nsew")
        self.table_scroll = customtkinter.CTkScrollbar(self.table_frame)
        self.table_scroll.grid(row=0, column=0, sticky="ns")
        self.table_frame.configure(self.table_scroll)



        # Crear entradas
        self.entry_funcion = customtkinter.CTkEntry(self.sidebar_frame, placeholder_text="Ingrese la función a evaluar",
                                                    width=200)
        self.entry_funcion.grid(row=1, column=0, pady=10, padx=10)
        self.entry_cotaInferior = customtkinter.CTkEntry(self.sidebar_frame, placeholder_text="Ingrese la cota inferior",
                                                    width=160)
        self.entry_cotaInferior.grid(row=2, column=0, pady=10, padx=10)
        self.entry_cotaSuperior = customtkinter.CTkEntry(self.sidebar_frame, placeholder_text="Ingrese la cota superior",
                                                    width=160)
        self.entry_cotaSuperior.grid(row=3, column=0, pady=10, padx=10)
        self.entry_tolerancia = customtkinter.CTkEntry(self.sidebar_frame, placeholder_text="Ingrese la tolerancia",
                                                    width=160)
        self.entry_tolerancia.grid(row=4, column=0, pady=10, padx=10)
        self.entry_ok = customtkinter.CTkButton(self.sidebar_frame, width=85, text="Aceptar", command=self.get_all_biseccion)
        self.entry_ok.grid(row=5, column=0, pady=10, padx=10)


        self.grafico = customtkinter.CTkCanvas(self.main_frame)
        self.grafico.grid(row=1, column=0)
        ###



    def get_all_biseccion(self):
        self.ecuacion = self.entry_funcion.get()
        self.Xa = float(self.entry_cotaInferior.get())
        self.Xb = float(self.entry_cotaSuperior.get())
        self.tolerancia = float(self.entry_tolerancia.get())
        self.evaluacion()
        self.total_rows = len(self.lst)
        self.total_columns = len(self.lst[0])
        self.Table(self.table_frame)



    def open_input_dialog_event(self):
        dialog = customtkinter.CTkInputDialog(text="Type in a number:", title="CTkInputDialog")
        print("CTkInputDialog:", dialog.get_input())

    def sidebar_button_event(self):
        print("sidebar_button click")

    def funcion(self, x):
        return eval (self.ecuacion)

    def evaluacion(self):
        graphic = plt.Figure(figsize=(5,4))
        graph = np.linspace((self.Xa - 10), (self.Xb + 10), 1000)
        graphic.add_subplot(111).plot(graph, self.funcion(graph))
        graphic.set_label("Grafico")
        chart = FigureCanvasTkAgg(graphic, self.grafico)
        chart.get_tk_widget().pack()
        while abs(self.f_c) >= self.tolerancia:
            puntoMedio = (self.Xa + self.Xb) / 2
            f_a = self.funcion(self.Xa)
            f_b = self.funcion(self.Xb)
            self.f_c = self.funcion(puntoMedio)

            self.iteraciones += 1
            print("Xa: ", self.Xa, "Xb: ", self.Xb, "c: ", puntoMedio, "f_c", self.f_c, "Número de iteraciones: ", self.iteraciones)
            self.lst += [(self.iteraciones, self.Xa, self.Xb, puntoMedio, self.f_c)]

            if (f_a * self.f_c) < 0:
                self.Xb = puntoMedio
            elif (f_b * self.f_c) < 0:
                self.Xa = puntoMedio
            if abs(self.f_c) < self.tolerancia:
                break
        print("La raíz buscada es: ", puntoMedio)


    def Table(self, main):
        # code for creating table
        for i in range(self.total_rows):
            for j in range(self.total_columns):
                self.e = Entry(main, width=10, fg='blue',
                               font=('Arial', 7))
                self.e.grid(row=i+1, column=j)
                self.e.insert(END, self.lst[i][j])







if __name__ == '__main__':
    app = App()
    app.mainloop()
    print("Hola Biseccion")









