#Algoritmo que pida los puntos centrales x1,y1,x2,y2 y los radios r1,r2 de dos 
#circunferencias y las clasifique en uno de estos estados:
#exteriores
#tangentes exteriores
#secantes
#tangentes interiores
#interiores
#concéntricas

x1 = float(input("Dime la coordenada x primera circunferencia: "))
y1 = float(input("Dime la coordenada y primera circunferencia: "))
r1 = float(input("Dime el radio  primera circunferencia: "))

x2 = float(input("Dime la coordenada x segunda circunferencia: "))
y2 = float(input("Dime la coordenada y segunda circunferencia: "))
r2 = float(input("Dime el radio segunda circunferencia: "))

import math
distancia = math.sqrt((x2-x1)**2 + (y1-y2)**2)

if distancia > (r1 + r2):
	print("circunferencias exteriores")

if distancia == (r1 + r2):
	print("circunferencias tangentes exteriores")

if distancia < (r1 + r2) and distancia > abs(r1-r2):
	print("Circunferencias tangentes secantes")

if distancia == abs(r1-r2):
	print("Circunferencias interiores")

if distancia == 0:
	print("Circunferencias concetricas")
