"""
 Crea una aplicación que permita adivinar un número. La aplicación genera un 
número aleatorio del 1 al 100. A continuación va pidiendo números y va 
respondiendo si el número a adivinar es mayor o menor que el introducido,
a demás de los intentos que te quedan (tienes 10 intentos para acertarlo). 
El programa termina cuando se acierta el número (además te dice en cuantos 
intentos lo has acertado), si se llega al limite de intentos te muestra el 
número que había generado.
"""
import random

num = random.randint(1, 100)

intentos = 0

while intentos <= 10:
	num_user = int(input("Adivina el número: "))
	if num == num_user:
		print("¡Bien, lo encontraste!")
		print("En", intentos, "intentos")
		break
	elif num_user < num:
		print("Uno mayor")
	else:
		print("Uno menor")
	intentos += 1

if intentos > 10:
	print("Perdiste")
