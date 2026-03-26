# Crear una función que calcule la temperatura media de un día a partir de la 
# temperatura máxima y mínima. Crear un programa principal, que utilizando la 
# función anterior, vaya pidiendo la temperatura máxima y mínima de cada día 
# y vaya mostrando la media. El programa pedirá el número de días que se van 
# a introducir.

def calcular_temperatura_media (tmin,tmax):
    return (tmin + tmax) / 2

cantidad = int (input('¿Cuántas temperaturas vas a calcular? : '))

for indice in range (cantidad):
    tmin = float(input("Introduce temperatura minima: "))
    tmax = float(input("Introduce temperatura máxima : "))

media = calcular_temperatura_media
print("Temperatura media:", media)

    