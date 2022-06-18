import math
from random import *
import numpy as np

def generar_bits(ls,li,presicion):
    return math.ceil( math.log( (ls-li)*10**presicion ,2) )

def generar_poblacion(numero_individuios, tamaño):
    poblacion = []

    for i in range(numero_individuios):
            cromosoma = []
            for j in range(tamaño):
                cromosoma.append( randint(0,1) )
            poblacion.append(cromosoma)
    print( np.array( poblacion ))
    return poblacion

def binario_a_decimal(array_binario):
    return int("".join(str(x) for x in array_binario), 2)

def calcular_x(x_prima, ls, li, bits):
    return li + ( (x_prima /((2**bits)-1) ) * (ls-li) )

def sustituir_en_formula(x1, x2):
    return x1**2 + x2**2

def calcular_calidades(poblacion):
    for i in range( len(poblacion)):
        x_prima1 = binario_a_decimal( poblacion[i][:22])
        x2_prima2 = binario_a_decimal(poblacion[i][23:45])
        x1 = calcular_x(x_prima1, 3, -3, bits)
        x2 = calcular_x(x2_prima2, 3, -3, bits)
        calidad = sustituir_en_formula(x1, x2)
        #print(calidad)
        poblacion[i].append(calidad)

    return poblacion

def torneo(t, poblacion, bits):
    index_calidad = bits*2 # index = 46
    r = randint(0, len(poblacion)-1)
    mejor = poblacion[r]
    
    for i in range(t):
        r2 = randint(0, len(poblacion)-1)
        contrincante = poblacion[r2]
        #print("contrincante: ",contrincante[index_calidad], "vs Mejor: ", mejor[index_calidad] )
        if contrincante[index_calidad] < mejor[index_calidad]:
            mejor = contrincante

    return mejor

def cruza_uniforme(padre1, padre2):
    hijo1 = []
    hijo2 = []
    for i in range(46): # tamaño del cromosoma
        if random() > .5:
            #hijo 1
            hijo1.append(padre1[i])
            hijo2.append(padre2[i])
        else:
            hijo1.append(padre2[i])
            hijo2.append(padre1[i])
    return [hijo1, 
            hijo2]

def limpiar_calidad(padre1, padre2):
    hijo1 = padre1[:46]
    hijo2 = padre2[:46]
    return [hijo1, 
            hijo2]

def mutar_hijos(hijos, probabilidad_de_mutacion):
    hijo1 = hijos[0]
    hijo2 = hijos[1]
    for i in range(len(hijo1)):
        if random() < probabilidad_de_mutacion:
            hijo1[i] = int(not hijo1[i])
    
    for i in range(len(hijo2)):
        if random() < probabilidad_de_mutacion:
            hijo2[i] = int(not hijo2[i])

    return [hijo1, hijo2]

def encontrar_mejor_individuo(poblacion):
    index_calidad = 46
    mejor = poblacion[0]
    for i in range( len(poblacion) ):
        if mejor[index_calidad] > poblacion[i][index_calidad]:
            mejor = poblacion[i]
    return mejor

    

bits = generar_bits(3, -3, 6)
t = 9
gen_max = 600
probabilidad_de_cruza = .9
probabilidad_de_mutacion = .01
print(bits)
n = 100
poblacion = generar_poblacion(n,bits*2)
poblacion = calcular_calidades(poblacion)

mejor_individuo = encontrar_mejor_individuo(poblacion)
gen = 1
while gen < gen_max and mejor_individuo[46] > 0.000001:
    j = 1
    while j < n:
        nueva_generacion = []
        padre1 = torneo(t, poblacion, bits)
        padre2 = torneo(t, poblacion, bits)
        #print("padre1: ", padre1, "padre2: ", padre2)

        if random() < probabilidad_de_cruza:
            hijos = cruza_uniforme(padre1, padre2)
        else:
            hijos = limpiar_calidad(padre1, padre2)


        if random() < probabilidad_de_mutacion:
            hijos = mutar_hijos(hijos, probabilidad_de_mutacion)

        

        hijos = calcular_calidades(hijos)
        nueva_generacion.append(hijos[0])
        nueva_generacion.append(hijos[1])
        j += 2

    mejor_individuo_nueva_generacion = encontrar_mejor_individuo(nueva_generacion)
    if mejor_individuo_nueva_generacion[46] < mejor_individuo[46]:
        mejor_individuo = mejor_individuo_nueva_generacion
    print(mejor_individuo)
    gen +=1

print("El mejor individuo es: ", mejor_individuo, "en ", gen, " generaciones")
