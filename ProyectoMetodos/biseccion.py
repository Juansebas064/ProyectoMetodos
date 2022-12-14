# Proyecto final métodos numéricos
# Ingeniería de sistemas - Univalle
# Integrantes: 
# Juan Felipe Arango Guzmán - 2060066 (Gauss-Seidel)
# Carlos Eduardo Guerrero Jaramillo - 2060216 (Bisección)
# Miguel Ángel Rivera Reyes - 2059876 (Newton-Raphson)
# Juan Sebastián Ruiz Aguilar - 2059898 (Punto fijo)

# Este método está implementado en el archivo gui.py

# Este archivo fue una prueba para implementarlo en la gui
#   principal

import math
import tkinter.messagebox
import tkinter as tk
import customtkinter
import matplotlib.pyplot as plt
import numpy as np
from tkinter import *
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from math import e,sin,cos,tan, pi

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")



class App(customtkinter.CTk):

    def __init__(self):

        super().__init__()


        # configure window
        self.ecuacion = ""
        self.Xa = 0.0
        self.Xb = 0.0
        self.puntoMedio=0.0
        self.iteraciones = 0
        self.error=0.0
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
        self.sidebar_frame.grid_rowconfigure(7, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Bisección",
                                                 font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))


        # main frame
        self.main_frame = customtkinter.CTkFrame(self, width=600, corner_radius=0)
        self.main_frame.grid(row=0, column=1, rowspan=4, sticky="nsew", padx=25)

        # table internal table frame

        self.table_frame = customtkinter.CTkFrame(self.main_frame, height=400, width=80)
        self.table_frame.grid(row=2, column=4, padx=25)



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
        self.entry_reset = customtkinter.CTkButton(self.sidebar_frame, width=85, text="Salir",
                                                command=self.reset_all_fields, state="disabled")
        self.entry_reset.grid(row=6, column=0, pady=10, padx=10)



        self.grafico_t = customtkinter.CTkLabel(self.main_frame,height=17, text="Gráfico", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.grafico_t.grid(row=1, column=0, sticky="nw")
        self.grafico = customtkinter.CTkCanvas(self.main_frame)
        self.grafico.grid(row=2, column=0)
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
        self.entry_ok.configure(state="disabled")
        self.entry_reset.configure(state="normal")


    def reset_all_fields(self):
        self.destroy()


    def open_input_dialog_event(self):
        dialog = customtkinter.CTkInputDialog(text="Type in a number:", title="CTkInputDialog")
        print("CTkInputDialog:", dialog.get_input())

    def sidebar_button_event(self):
        print("sidebar_button click")

    def funcion(self, x):
        return eval (self.ecuacion)

    def evaluacion(self):
        self.lst += [("Iteraciones", "An", "Bn", "Pn", "F(Pn)", "Error")]
        #graphic = plt.Figure(figsize=(5,4))
        x1 = np.linspace((self.Xa - 10), (self.Xb + 10), 1000)

        y = list(map(lambda x: self.funcion(x), x1))

        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)

        plt.plot(x1, y)
        plt.plot(self.puntoMedio, self.funcion(self.puntoMedio), marker="o")

        chart = FigureCanvasTkAgg(fig, self.grafico)
        chart.get_tk_widget().pack()
        while abs(self.f_c) >= self.tolerancia:
            raizA = self.puntoMedio
            self.puntoMedio = (self.Xa + self.Xb) / 2
            f_a = self.funcion(self.Xa)
            f_b = self.funcion(self.Xb)
            self.f_c = self.funcion(self.puntoMedio)
            self.error=(abs((self.puntoMedio - raizA)/self.puntoMedio))
            self.iteraciones += 1
            print("Xa: ", self.Xa, "Xb: ", self.Xb, "c: ", self.puntoMedio, "f_c", self.f_c, "Número de iteraciones: ", self.iteraciones)
            self.lst += [(self.iteraciones, self.Xa, self.Xb, self.puntoMedio, self.f_c, self.error)]

            if (f_a * self.f_c) < 0:
                self.Xb = self.puntoMedio
            elif (f_b * self.f_c) < 0:
                self.Xa = self.puntoMedio
            if abs(self.f_c) < self.tolerancia:
                break
        print("La raíz buscada es: ", self.puntoMedio)
        self.raizfinal = customtkinter.CTkLabel(self.table_frame, text=("La raíz buscada es aproximadamente: "+ str(self.puntoMedio)))
        self.raizfinal.grid(row=0, column=0, pady=10, columnspan=7)
        self.nIter = customtkinter.CTkLabel(self.table_frame, text=("Iteraciones para encontrar la raíz: " + str(self.iteraciones)))
        self.raizfinal.grid(row=1, column=0, pady=10, columnspan=7)


    def Table(self, main):
        # code for creating

        for i in range(self.total_rows):
            for j in range(self.total_columns):
                self.scrollbar = tk.Scrollbar(orient="horizontal")
                self.e = Entry(main, width=10, fg='blue',
                             font=('Arial', 7), xscrollcommand=self.scrollbar.set)
                self.e.focus()
                self.scrollbar.config(command=self.e.xview)
                self.e.config()
                self.e.grid(row=i+3, column=j)
                self.e.insert(END, self.lst[i][j])
                self.scrollbar.config(command=self.e.xview)
                self.e.config()

if __name__ == '__main__':
    app = App()
    app.mainloop()









