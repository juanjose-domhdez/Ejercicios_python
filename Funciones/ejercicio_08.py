# Crear una función recursiva que permita calcular el factorial de un número. 
# Realiza un programa principal donde se lea un entero y se muestre el resultado 
# del factorial.

def CalcularFactorial(n):
    if n < 0:
        return None
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

numero1 = int(input("Número: "))
print(f"El factorial es: {CalcularFactorial(numero1)}")