#Crea un programa que pida dos número enteros al usuario y diga si alguno de ellos 
#es múltiplo del otro. Crea una función EsMultiplo que reciba los dos números, 
#y devuelve si el primero es múltiplo del segundo.

def EsMultiplo(a, b):
    if b == 0:
        return False 
    return a % b == 0

numero1 = int(input("Número 1: "))
numero2 = int(input("Número 2: "))

if EsMultiplo(numero1, numero2):
    print(f"{numero1} es múltiplo de {numero2}")
else:
    print(f"{numero1} no es múltiplo de {numero2}")