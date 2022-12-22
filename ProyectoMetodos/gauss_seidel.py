# Proyecto final métodos numéricos
# Ingeniería de sistemas - Univalle
# Integrantes: 
# Juan Felipe Arango Guzmán - 2060066 (Gauss-Seidel)
# Carlos Eduardo Guerrero Jaramillo - 2060216 (Bisección)
# Miguel Ángel Rivera Reyes - 2059876 (Newton-Raphson)
# Juan Sebastián Ruiz Aguilar - 2059898 (Punto fijo)

import tkinter as tk

funcion = 0

a11 = 0
a12 = 0
a13 = 0
a21 = 0
a22 = 0
a23 = 0
a31 = 0
a32 = 0
a33 = 0

x1 = 0
x2 = 0
x3 = 0

b1 = 0
b2 = 0
b3 = 0

tolerancia = 0.0001

vectorS = []

x1anterior = 0
x2anterior = 0
x3anterior = 0

vectorSAnterior = []


#Esta funcion verifica que la matriz sea diagonalmente dominante
def FunDiagDom3x3():
    if abs(a11) >= (abs(a12)+abs(a13)) and abs(a22) >= (abs(a21)+abs(a23)) and abs(a33) >= (abs(a31)+abs(a32)):
        return True

    else:
        return False


def FunDiagDom2x2():
    if abs(a11) >= (abs(a12)) and abs(a22) >= (abs(a21)):
        return True

    else:
        return False


#La funcion calcula un paso de iteracion del vector solucion
def Calcular3x3():


    global x1anterior
    global x1
    global x2anterior
    global x2
    global x3anterior
    global x3
    global vectorS
    global vectorSAnterior

    if FunDiagDom3x3 ():
        

        if a11 != 0:
            
            x1anterior = x1
            x1 = (b1 -(a12*x2) -(a13*x3))/a11
            print(f"x1={x1}")

        else:
            print("La posicion a11 no debe ser 0")

        
        if a22 != 0:

            
            x2anterior = x2
            x2 = (b2 -(a21*x1) -(a23*x3))/a22
            print(f"x2={x2}")

        else:
            print("La posicion a22 no debe ser 0")


        if a33 != 0:
            
            x3anterior = x3
            x3 = (b3 -(a31*x1) -(a32*x2))/a33
            print(f"x3={x3}\n")

        else:
            print("La posicion a33 no debe ser 0")

        vectorSAnterior = [x1anterior,x2anterior,x3anterior]
        vectorS = [x1,x2,x3]
    else:
        print("La matriz debe ser diagonalmente dominante")

#La funcion calcula un paso de iteracion del vector solucion
def Calcular2x2 ():

    global x1
    global x1anterior
    global x2
    global x2anterior
    global vectorS
    global vectorSAnterior

    if FunDiagDom2x2():

        

        if a11 != 0:

            x1anterior = x1
            x1 = (b1-(a12*x2))/a11

        else:
            print("a11 no debe ser 0")

        
        if a22 != 0:

            x2anterior = x2
            x2 = (b2-(a21*x1))/a22

        vectorSAnterior = [x1anterior,x2anterior]
        vectorS = [x1,x2]



#La funcion calcula el error entre cada iteracion del vector solucion con la norma infinito
def CalcularError ():
    vector_nuevo = []
    for i in range(0,len(vectorS)):
        vector_nuevo.insert(i,abs(vectorS[i]- vectorSAnterior[i]))
    error = max(vector_nuevo)/max(vectorS)
    return error 

#Dependiendo del tamaño de sistema que se escoja repite la funcion calcular hasta que el error sea menor o igual a la tolerancia deseada
def gauss_seidel():

    if funcion == 0:
        Calcular3x3()
    elif funcion == 1:
        Calcular2x2()

    error = CalcularError()
    while error > tolerancia:

        if funcion == 0:
            Calcular3x3()
        elif funcion == 1:
            Calcular2x2()

        error = CalcularError()




