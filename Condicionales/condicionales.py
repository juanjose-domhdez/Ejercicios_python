# COndicionales con Phyton

# if, else, elif

"""
if exp_bool:
	instrucciones

if exp_bool:
	instrucciones
else:
	instrucciones

if exp_bool:
	instrucciones
elif expo_bool:
	instrucciones
else:
	instrucciones
"""

print("Inicio")

numero = int(input("Ingresa un un numero: "))

if numero > 0:
	print("Es un numero positivo")
elif numero	== 0:
	print("Es cero")
else:
	print("No es un numero positivo")

print("Fin")