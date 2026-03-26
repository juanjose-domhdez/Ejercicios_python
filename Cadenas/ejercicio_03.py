# Se quiere realizar un programa que lea por teclado las 5 notas obtenidas por un 
# alumno (comprendidas entre 0 y 10). A continuación debe mostrar todas las notas, 
# la nota media, la nota más alta que ha sacado y la menor.

frase = input("Ingresa una frase: ")
letra = input("Ingresa una letra: ")
while len(letra) != 1:
    letra = input("Ingresa una letra: ")
count = 0
for i in frase:
    if 1 == letra:
        count += 1

print(f"La letra '{letra}' esta '{count}' veces en '{frase}'")