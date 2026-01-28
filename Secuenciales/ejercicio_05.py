#Escribe un programa que convierta el valor dado en grados Farenheit a
# Celsius

print("Conversion de Fahrenheit a Celsius")
farenheit = float(input("Ingresa los grados Fahrenheit: "))
celsius = (farenheit - 32) * (5 / 9)

print("Grados Fahrenheit", farenheit)
print("Grados Celsius", celsius)

print(f'{ farenheit }°F equivale a { celsius }°C')