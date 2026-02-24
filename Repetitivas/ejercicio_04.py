"""
Realizar un algoritmo que pida números (se pedirá por teclado la cantidad de 
números a introducir). El programa debe informar de cuantos números introducidos 
son mayores que 0, menores que 0 e iguales a 0.
"""
igual_0 = 0
mayor_0 = 0
menor_0 = 0

cant_num = int(input("¿Cuantos numeros vas a introducir"))

for i in range(cant_num):
	num = int(input("Ingresa un numero: "))
	if num == 0:
		igual_0 += 1
	elif num < 0:
		menor_0 += 1
	else:
		mayor_0 += 1
print("Ingresaste", igual_0, "ceros")
print("Ingresaste", mayor_0, "menores a cero")
print("Ingresaste", menor_0, "menores a cero")
