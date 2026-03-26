'''

Listas 
-con corchetes-
[1, 3, 5, 7, 8]
['a', 'b', 'c', 'd']
[True, False, False, True]
[1, 0, 'a', True, [1, 2]]

'''


pares = [0, 2, 4, 6, 8, 10] #Valor 0 es el 1
impares = [1, 3, 5, 7, 9, 11]

print(type(pares))

print(pares[0])
print(pares[2])
print(pares[-1])

for i in impares:
    print(i)

impares.append(25) #inserta elementos al final
print(impares)
impares.pop() # extrae el ultimo
print(impares)
impares.reverse() # invierte la lista
print(impares)
impares.sort() #ordena la lista
print(impares)
