#Pedir el nombre y los dos apellidos de una persona y mostrar las iniciales.

nombre = input("Dime tu nombre: ")
apellido = input("Dime tu primer apellido: ")
apellido2 = input("Dime tu segundo apellido: ")

inicial = nombre[0] + apellido[0] + apellido2[0]

inicial = inicial.upper()

print("Las iniciales son:", inicial)
