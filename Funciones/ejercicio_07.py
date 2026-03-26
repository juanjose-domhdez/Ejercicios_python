# Crear una subrutina llamada "Login", que recibe un nombre de usuario y una 
# contraseña y te devuelve Verdadero si el nombre de usuario es "usuario1" y la 
# contraseña es "asdasd". Además recibe el número de intentos que se ha intentado 
# hacer login y si no se ha podido hacer login incremente este valor.
# Crear un programa principal donde se pida un nombre de usuario y una contraseña 
# y se intente hacer login, solamente tenemos tres oportunidades para intentarlo.

def login(usuario,clave,intentos):
    usuario_correcto = "Yan"
    clave_correcta = "yan0306"

    intentos += 1
    if usuario == usuario_correcto and clave == clave_correcta:
        return True,intentos
    else:
        return False,intentos
    
intentos = 0
entrar = False

while not entrar and intentos < 3:
    usuario = input("usuario: ")
    clave = input("password: ")

    entrar, intentos = login(usuario,clave,intentos)
    if not entrar:
        print("Error, Nombre de usuario o contraseña incorrecta.")

    if entrar:
        print("Bienvenidos al sistema")
    else:
        print("No has entrado al sistema")
