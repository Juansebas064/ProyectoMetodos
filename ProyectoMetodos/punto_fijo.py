#
# Juan Sebastián Ruiz Aguilar
# Métodos numéricos
# Univalle Tuluá
#

# Importamos las librerías necesarias
#import sympy as sp
from sympy import Eq, Interval, Reals, Set, lambdify, symbols, sympify, calculus, plot, sqrt, plot_implicit
from sympy import sin, cos, tan, pi, euler as e


# Definición de la función punto_fijo(). 
def punto_fijo(funcion: str,extremo_izq: str,extremo_der: str,x_inicial: str,iteraciones: str, error: float):
    
    logs = []

    # Creación del intervalo, la función y el dominio
    ext_i, ext_d = float(sympify(extremo_izq,evaluate=True)), float(sympify(extremo_der,evaluate=True))
    intervalo = Interval(ext_i,ext_d)
    x = symbols('x')
    fun = Eq(sympify(funcion),0)  # Esta función se usa para calcular el dominio
    f = lambdify(x,funcion)  # Esta función se usa para evaluar valores de x en la función
    dominio = calculus.util.continuous_domain(fun,x,Reals)

    # Comprobación teorema de existencia y unicidad de punto fijo

    # Existencia:

    # Evaluamos si la función es continua en el intervalo dado
    continua: bool
    if intervalo.is_subset(dominio):
        continua = True
        logs.append("La función es continua")
    else:
        logs.append("Error: La función no es continua")
        return logs, ""

    # Evaluamos si las imágenes de f en el intervalo están contenidas en el intervalo
    rango_dentro_intervalo: bool
    if (max(f(ext_i),f(ext_d)) <= ext_d) and (min(f(ext_i),f(ext_d)) >= ext_i): 
        rango_dentro_intervalo = True
        logs.append("Las imágenes están dentro del intervalo")
    else:
        logs.append("Error: Las imágenes no están dentro del intervalo")
        return logs, ""
    

    # Calculamos el punto fijo con las iteraciones de la función

    x_actual = 0
    x_anterior = float(x_inicial) if len(x_inicial) != 0 else (float(ext_i)+float(ext_d))/2
    i = int(iteraciones) if len(iteraciones) != 0 else 100
    contador = 0

    
    while(contador < i):
        x_actual = f(x_anterior)
        logs.append(f"#{contador+1}: {x_actual}, error = {abs(x_actual-x_anterior)}\n")
        if abs(x_actual-x_anterior) <= error:
            logs.append(f"Punto fijo en la iteración #{contador+1} = {x_actual}\n")
            print("\n")
            return logs, x_actual
        x_anterior = x_actual
        contador+=1
    logs.append(f"No se encontró un punto fijo en {contador} iteraciones para la función {funcion} en el intervalo [{extremo_izq},{extremo_der}]\n")

    return logs, ""


# Llamados de la función

#punto_fijo(input("Ecuación: "),input("Extremo izquierdo del intervalo: "),input("Extremo derecho del intervalo: "),input("Máximo de iteraciones deseadas (opcional): "),input("Error: "))
#print(punto_fijo("1+e**-x",1,2,"","",0.00001))
#punto_fijo("1/3*(x**2-1)",-1,1,"","9",0.000001)
#punto_fijo("x**2-2",-1,2,"-0.5","",0.000001)