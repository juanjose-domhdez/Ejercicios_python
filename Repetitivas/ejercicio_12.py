"""
Realizar un algoritmo para determinar cuánto ahorrará una persona en un año, 
si al final de cada mes deposita cantidades variables de dinero; 
además, se quiere saber cuánto lleva ahorrado cada mes.
"""
mes = int(1)
ahorro_acum = 0

for mes in range (1, 13):
	cant_mensual = int(input("¿Cuanto has ahorrado en el mes? ",mes))
	ahorro_acum = ahorro_acum +  cant_mensual
	print("En el mes", mes, "llevas ahorrado ",ahorro_acum)
	mes += 1