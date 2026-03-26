'''
Realizar un programa que comprueba si una cadena leída por teclado comienza por 
una subcadena introducida por teclado.
'''
cad = input("Escribe una frase: ")
subcad = input("Escribe una subcadena: ")

if cad.startswith(subcad):
    print(f"{cad} comienza con {subcad}")
else:
    print(f"{cad} no comienza con {subcad}")