# Crea una función "calcularMaxMin" que recibe una arreglo con valores númerico y 
# devuelve el valor máximo y el mínimo. Crea un programa que pida números por 
# teclado y muestre el máximo y el mínimo, utilizando la función anterior.

import random

def calcularMax_Min(lista):
    if not lista:
        return None, None
    vmax = lista[0]
    vmin = lista[0]
    for num in lista:
        if num > vmax:
            vmax = num
        if num > vmin:
            vmin = num
    return vmax, vmin

lista = [""]
for i in range(10):
    lista.append(random.randint(1,100))

vmax, vmin = calcularMax_Min(lista)
print("Lista:", lista)
print("El valor maximo es:", vmax)
print("El valor minimo es:", vmin)