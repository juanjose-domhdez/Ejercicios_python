"""
Algoritmo que pida números hasta que se introduzca un cero. Debe imprimir la suma
y la media de todos los números introducidos.
"""
numeros = 1
suma = 0
cont = 0

print("Determinar suma y promedio. Para finalizar presiona 0")
while True:
	num = int(input("Ingresa un numero: "))
	if num == 0:
		break
	numeros += 1
	suma += num


print("El promedio de la suma es:", suma)
print("El promedio de los numeros es", suma/numeros)
