"""
Escribe un programa que diga si un número introducido por teclado es o no primo. 
Un número primo es aquel que sólo es divisible entre él mismo y la unidad. 
Nota: Es suficiente probar hasta la raíz cuadrada del número para ver si es 
divisible por algún otro número.
"""
es_primo = True
numero_es_primo = int(input("Introduce un numero para comprobar si es primo: "))

import math

for num in range(2, int(numero_es_primo **0.5) + 1):
	if (numero_es_primo % num == 0):
		es_primo = False

	if es_primo:
		print("Es primo")
	else:
		print("No es primo")
