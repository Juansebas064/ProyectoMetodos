#
# Juan Sebastián Ruiz Aguilar
# Métodos numéricos
# Univalle Tuluá
#

# Importamos las librerías necesarias
import sympy as sp
from sympy import Set
from math import sin, cos, tan, pi, e


# Definición de la función punto_fijo(). 
def punto_fijo(funcion: str,extremo_izq: int,extremo_der: int,x_inicial: str,iteraciones: str, error: float):
    
    # Creación del intervalo, la función y el dominio
    ext_i, ext_d = sp.sympify(extremo_izq), sp.sympify(extremo_der)
    intervalo = sp.Interval(ext_i,ext_d)
    x = sp.symbols('x')
    fun = sp.Eq(sp.sympify(funcion),0)  # Esta función se usa para calcular el dominio
    f = sp.lambdify(x,funcion)  # Esta función se usa para evaluar valores de x en la función
    dominio = sp.calculus.util.continuous_domain(fun,x,sp.Reals)

    # Comprobación teorema de existencia y unicidad de punto fijo

    # Existencia:

    # Evaluamos si la función es continua en el intervalo dado
    continua: bool
    if intervalo.is_subset(dominio):
        continua = True
        print("La función es continua")
    else:
        print("No se puede hacer punto fijo")
        return "No se puede hacer punto fijo", "F"

    # Evaluamos si las imágenes de f en el intervalo están contenidas en el intervalo
    rango_dentro_intervalo: bool
    if (max(f(ext_i),f(ext_d)) <= ext_d) and (min(f(ext_i),f(ext_d)) >= ext_i): 
        rango_dentro_intervalo = True
        print("Las imágenes están dentro del intervalo")
    else:
        print("No se puede hacer punto fijo")
        return "No se puede hacer punto fijo", "F"

    # Unicidad:

    # Derivamos f y vemos si existe para todo x en (a,b)
    

    # Calculamos el punto fijo con las iteraciones de la función

    x_actual = 0
    x_anterior = float(x_inicial) if len(x_inicial) != 0 else (extremo_der+extremo_der)/2
    i = int(iteraciones) if len(iteraciones) != 0 else 100
    contador = 0
    
    while(contador < i):
        x_actual = f(x_anterior)
        print(f"#{contador+1}: {x_actual}, error = {abs(x_actual-x_anterior)}")
        if abs(x_actual-x_anterior) <= error:
            print(f"Punto fijo en la iteración #{contador+1} = {x_actual}")
            print("\n")
            return f"Punto fijo en la iteración #{contador+1} = {x_actual}", x_actual
        x_anterior = x_actual
        contador+=1
    
    return f"No se encontró un punto fijo en {contador} iteraciones para la función {funcion} en el intervalo [{extremo_izq},{extremo_der}]\n", "F"


# Llamados de la función

#punto_fijo(input("Ecuación: "),input("Extremo izquierdo del intervalo: "),input("Extremo derecho del intervalo: "),input("Máximo de iteraciones deseadas (opcional): "),input("Error: "))
#print(punto_fijo("1+e**-x",1,2,"","",0.00001))
#punto_fijo("1/3*(x**2-1)",-1,1,"","9",0.000001)
#punto_fijo("x**2-2",-1,2,"-0.5","",0.000001)