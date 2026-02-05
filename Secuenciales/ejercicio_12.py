# Pide al usuario dos pares de números x1,y2 y x2,y2, que representen dos puntos
# en el plano. Calcula y muestra la distancia entre ellos.

x1 = int(input("Dime las coordenadas del punto 1: "))
y1 = x1

x2 = int(input("Dime las coordendas del punto 2: "))
y2 = x2

distancia = ((x2-x1)^2 + (y2-y1^2)) **0.5

print("Distancia:",distancia)
