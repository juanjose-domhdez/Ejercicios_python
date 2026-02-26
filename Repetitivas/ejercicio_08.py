"""
Escribe un programa que pida el limite inferior y superior de un intervalo. 
Si el límite inferior es mayor que el superior lo tiene que volver a pedir.
A continuación se van introduciendo números hasta que introduzcamos el 0. 
Cuando termine el programa dará las siguientes informaciones:
* La suma de los números que están dentro del intervalo (intervalo abierto).
* Cuantos números están fuera del intervalo.
* He informa si hemos introducido algún número igual a los límites del intervalo.
"""
suma_dentro_intervalo = 0
cont_fuera_intervalo = 0
igual_limites = "Falso"
while True:
	lim_inf = int(input("Introduce el limite inferior del intervalo: "))
	lim_sup = int(input("Introduce el limite superior del intervalo: "))
	if lim_inf > lim_sup:
		print("ERROR: El limite inferior debe ser menor que el superior")
	if lim_inf <= lim_sup:
		break

while True:
	num = int(input("Introduce un numero (0, para salir): "))
	if num == 0:
		break
	if num > lim_inf and num < lim_sup:
		suma_dentro_intervalo = (suma_dentro_intervalo + num)
	else:
		cont_fuera_intervalo = (cont_fuera_intervalo + 1)

	if num == lim_inf or num == lim_sup:
		igual_limites = "Verdadero"

print("La suma de los numeros dentro del intervalo es ", suma_dentro_intervalo)
print("La cantidad de numeros fuera del intervalo es ", cont_fuera_intervalo)
if igual_limites == "Verdadero":
	print("Se ha introducido algun numero igual a los limites del intervalo")
else:
	print("No se ha introducido ningun numero igual a los limites del intervalo")
