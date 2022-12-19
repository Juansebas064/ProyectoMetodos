# Proyecto final métodos numéricos
# Ingeniería de sistemas - Univalle
# Integrantes: 
# Juan Felipe Arango Guzmán - 2060066 (Gauss-Seidel)
# Carlos Eduardo Guerrero Jaramillo - 2060216 (Bisección)
# Miguel Ángel Rivera Reyes - 2059876 (Newton-Raphson)

import numpy as np
import sympy as sp
import math as mt


def datos():

   f = input("Ingrese la funcion a calcular: ")

   while(True):

       try:
           x0 = float(input("Ingrese el numero de inicio: "))

           tao = float(input("Ingrese una tolearancia: "))
           break
        
       except:
            print("algo salio mal, ingrese los valores bien")
   newtonRaphson(f,x0,tao)




def newtonRaphson(f, x0, tol):

        x = sp.Symbol('x')
   
        derivadaf = sp.diff(f)
        f = sp.lambdify(x, f,"math")
        print(derivadaf)
        derivadaf = sp.lambdify(x,derivadaf,"math")

       
        print(str(abs(derivadaf(x0))) +" " +str(x0))
        if(True):
            k=0
            while(True):

                if(derivadaf(x0) !=0):
 
                        x1 = x0-f(x0)/derivadaf(x0)

                        if( abs(x1-x0) <= tol):
                            print("X", k+1, "=", x1, end=" ")
                            
                            print("Es una buena aproxde la raiz")
                            break
                        x0=x1
                        k+=1
                        print("X", k+1, "=", x1)
                        
                else:
                    print("la derivada se vuelve 0, no es posible realizar el metodo ya que pasa por:" + str(x0)+ " pruebe con otro valor inicial(no converge)")
                    break
        else:
                    print("EL METODO NO CONVERGE")
                    print(str(abs(derivadaf(x0))) +" " +str(x0))
                    


##print(e)

##newtonRaphson(mt.pi, 0.0000000001,20)

datos()