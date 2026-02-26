#Un ciclista parte de una ciudad A a las HH horas, MM minutos y SS segundos. 
#El tiempo de viaje hasta llegar a otra ciudad B es de T segundos. 
#Escribir un algoritmo que determine la hora de llegada a la ciudad B.

horapartida = int(input("Hora de salida: "))
minpartida = int(input("Minutos de salida: "))
segpartida = int(input("Segundos de salida: "))
segviaje = int(input("Tiempo que has tardado en segundos: "))

seginicial = horapartida * 3600 + minpartida*60 +segpartida
segfinal = seginicial + segviaje

import math
horallegada = math.trunc(segfinal / 3600)
minllegada = int(math.trunc(segfinal % 3600) / 60)
segllegada = (segfinal % 3600) % 60

text = f"Hora de llegada {horallegada}:{minllegada}:{segllegada}"
print(text)
