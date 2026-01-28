#Carcular el perimetro y area de un rectangulo dada su base y su altura

# input regresa un string para hacer operaciones se debe
# convertir

#int()-entero

print("Calculo de Area y Perimetro de un Rectangulo")
base = input("Ingresa la base: ")
base = int(base)

height = input("Ingresa la altura: ")
height = int(height)

area = base * height
perimeter = base + base + base + base 

print("Area:",area)
print("Perimetro:",perimeter)
