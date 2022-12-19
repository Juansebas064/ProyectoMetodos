# Proyecto final métodos numéricos
# Ingeniería de sistemas - Univalle
# Integrantes: 
# Juan Felipe Arango Guzmán - 2060066 (Gauss-Seidel)
# Carlos Eduardo Guerrero Jaramillo - 2060216 (Bisección)
# Miguel Ángel Rivera Reyes - 2059876 (Newton-Raphson)

import tkinter
import tkinter.messagebox
import customtkinter
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import matplotlib.pyplot as plt

customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"
import sympy as sp
import numpy as np
from prettytable import PrettyTable


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        
        self.title("Newton Rapthson")
        self.geometry(f"{1100}x{580}")

        
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="DATOS", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.funcionInput = customtkinter.CTkEntry(self.sidebar_frame, placeholder_text="Ingrese la funcion")
        self.funcionInput.grid(row=1, column=0, padx=20, pady=10)

        self.xInicialInput = customtkinter.CTkEntry(self.sidebar_frame, placeholder_text="Ingrese el valor inicial")
        self.xInicialInput.grid(row=2, column=0, padx=20, pady=10)

        self.tolInput = customtkinter.CTkEntry(self.sidebar_frame, placeholder_text="Ingrese la tolerancia")
        self.tolInput.grid(row=3, column=0, padx=20, pady=10)

        self.calcularButton = customtkinter.CTkButton(self.sidebar_frame, command=self.calcular,text="Calcular")
        self.calcularButton.grid(row=4, column=0, padx=20, pady=10)
        
        self.table_frame = customtkinter.CTkFrame(self,width=240)
        self.table_frame.grid(row=0, column=2,rowspan=4,padx=(10,10),pady=(10, 10),sticky="nsew")

        self.stringvar= customtkinter.StringVar()
  
        self.tablaf = customtkinter.CTkLabel(self.table_frame, textvariable=self.stringvar, font=customtkinter.CTkFont(size=20, weight="bold"))
        self.tablaf.pack(side="left",fill="both",expand=1)
       
        


    def newtonRaphson(self,f, x0, tol):
        
        global table
    
        
        table = PrettyTable()
        table.field_names = ["Xn"]
        


        x = sp.Symbol('x')

        try:
    
            derivadaf = sp.diff(f)
            f = sp.lambdify(x, f,"math")
            print(derivadaf)
           
            derivadaf = sp.lambdify(x,derivadaf,"math")
           
            print(str(abs(derivadaf(x0))) +" " +str(x0))

            k=0
            while(True):

                try:

                    if(derivadaf(x0) !=0):
        
                            x1 = x0-f(x0)/derivadaf(x0)

                            if( abs(x1-x0) <= tol):
                                print("X", k+1, "=", x1, end=" ")
                                    
                                table.add_row([x1])
                            #    print("Es la raiz")
                                return table, x1
                            x0=x1
                            k+=1
                            print("X", k+1, "=", x1)
                            table.add_row([x1])
                                
                            
                    else:
                        print("la derivada se vuelve 0, no es posible realizar el metodo ya que pasa por:" + str(x0)+ " pruebe con otro valor inicial(no converge)")
                        return [1]
                        break
                except:
                    return [2]
                    break
        except:
            return [0]



    def calcular(self):

        global tablaAll

        f =self.funcionInput.get()

       
        x0 = self.xInicialInput.get()
        tol = self.tolInput.get()

        if(len(f) !=0 and len(x0) !=0 and len(tol) !=0):

            if(f != " " and x0 != " " and tol != " "):

                try:

                    tol1 = float(tol)
                    x01 = float(x0)

                    if((float(tol) >=0 and float(tol) <1)):

                      #  print("soy tol, mi valor es {}, y soy {}".format(tol,tol.isnumeric()))

                        if(float(tol) >=0 and float(tol) <1):

                            
                            
                            tablaAll = self.newtonRaphson(f,float(x0),float(tol))

                            if(len(tablaAll)!=1):
                                

                                print(type(tablaAll))


                                x = sp.Symbol('x')
                                f = sp.lambdify(x, f,"math")

                            
                            
                            

                                try:
                                    x1=np.arange(-10,10,0.01)
                                    print(x1)

                                    y = list(map(lambda x: f(x),x1))
                                    print(y)

                                    fig = plt.figure()
                                    ax = fig.add_subplot(1, 1, 1)

                                    ax.spines['left'].set_position('center')
                                    ax.spines['bottom'].set_position('center')
                                    
                                    print(tablaAll[0])

                                    
                                # self.textbox.insert(customtkinter.END, text=tabla)

                                    plt.plot(x1,y)
                                    plt.plot(tablaAll[1],f(tablaAll[1]),marker ="o")

                                    
                                    
                                    self.stringvar.set(tablaAll[0]) 
                                

                                
                                    self.another_frame = customtkinter.CTkFrame(self,corner_radius=30)
                                    self.another_frame.grid(row=0, column=1, rowspan=4, sticky= "nsew")
                                    self.canvas = FigureCanvasTkAgg(fig, master=self.another_frame)
                                    self.canvas.draw()
                                    self.canvas.get_tk_widget().pack(side="left",fill="both",expand=1)

                                    toolbar = NavigationToolbar2Tk(self.canvas, self.another_frame)
                                    toolbar.update()
                                    self.canvas.get_tk_widget().pack(side =tkinter.TOP,fill=tkinter.BOTH, expand=1)
                                
                                except:

                                    x1=np.arange(0.1,10,0.01)
                                    print(x1)

                                    y = list(map(lambda x: f(x),x1))
                                    print(y)

                                    fig = plt.figure()
                                    ax = fig.add_subplot(1, 1, 1)

                                    ax.spines['left'].set_position('center')
                                    ax.spines['bottom'].set_position('center')
                                    
                                    print(tablaAll[0])

                                    
                                # self.textbox.insert(customtkinter.END, text=tabla)

                                    plt.plot(x1,y)
                                    plt.plot(tablaAll[1],f(tablaAll[1]),marker ="o")


                                    self.stringvar.set(tablaAll[0]) 
                                            

                                    self.another_frame = customtkinter.CTkFrame(self,corner_radius=30)
                                    self.another_frame.grid(row=0, column=1, rowspan=4, sticky= "nsew")
                                    self.canvas = FigureCanvasTkAgg(fig, master=self.another_frame)
                                    self.canvas.draw()
                                    self.canvas.get_tk_widget().pack(side="left",fill="both",expand=1)

                                    toolbar = NavigationToolbar2Tk(self.canvas, self.another_frame)
                                    toolbar.update()
                                    self.canvas.get_tk_widget().pack(side =tkinter.TOP,fill=tkinter.BOTH, expand=1)


                            else:
                                if(tablaAll[0]==0):
                                    self.stringvar.set("verifique que la funcion este bien escrita ")
                                else:
                                    self.stringvar.set("La fUNCION NO CONVERGE ")
                        else:
                            self.stringvar.set("La tolerancia debe ser un numero menor o igual a 0")
                    else:
                        self.stringvar.set("INGRESE DATOS VALIDOS")
                except:

                        self.stringvar.set("Ingrese una tolerancia valida")
            else:
                self.stringvar.set("ingrese datos validos")
        else:
            self.stringvar.set("ingrese datos validos")


        
if __name__ == "__main__":
    app = App()
    app.mainloop()