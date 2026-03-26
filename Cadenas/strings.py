'''
Strings con python
'''
name = "Francisco"
profession = 'Profesor'

greetings = "Hello I'm Francisco"
print(greetings)
traslate = '"Hello" es "Hola"'
print(traslate)

# Escapar caracteres con 
#Cambiar el sentido del caracter

greetings = 'Hello I\'m Francisco'
print(greetings)

menu = 'Elige una opcion: \n1.- Op1\n2.- Op2'
print(menu)

# String Format
message1 = "Hello I'm {} and I'm {}".format(name, profession)
print(message1)
message2 = f"Hello I'm { name } and I'm { profession }"
print(message2)

# Metodos para strings
movie = "Volver al futuro"
print(movie)
print(movie.upper())
print(movie.lower())
print(movie.capitalize())
print(movie.title())
print(movie.split(" "))
print(movie.startswith("V"))
print(movie.endswith("V"))
print("a" in movie)
