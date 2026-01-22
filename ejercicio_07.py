# Realiza un programa que reciba una cantidad de minutos y muestre por pantalla a
# cuantas horas y minutos corresponde

print("Calcular Horas")

minutos = int(input("Dame la cantidad de minutos: "))
res_horas = int
res_min = int

res_horas = (minutos // 60)
res_min = (minutos % 60)

print(res_horas," horas y",res_min, " minutos.")
