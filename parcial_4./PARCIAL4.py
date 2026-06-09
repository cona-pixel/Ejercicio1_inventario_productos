
usuarios = {}
def validar_contrasena(contrasena):
    tiene_numero = False
    tiene_letra = False

    if len(contrasena) < 8:
        return False

    if " " in contrasena:
        return False

    for caracter in contrasena:
        if caracter.isdigit():
            tiene_numero = True
        if caracter.isalpha():
            tiene_letra = True

    if tiene_numero and tiene_letra:
        return True
    else:
        return False

def ingresar_usuario():
    while True:
        nombre = input("Ingrese nombre de usuario: ").lower()

        if nombre in usuarios:
            print("Usuario ya existe. Intente otro.")
        else:
            break

    while True:
        sexo = input("Ingrese sexo: ").upper()

        if sexo == "F" or sexo == "M":
            break
        else:
            print("Debe ingresar M o F solamente. Intente de nuevo.")

    while True:
        contrasena = input("Ingrese contraseña: ")

        if validar_contrasena(contrasena):
            print("Contraseña valida.")
            break
        else:
            print("Contraseña no valida. Intente otra.")

    usuarios[nombre] = {
        "sexo": sexo,
        "contrasena": contrasena
    }

    print("Usuario ingresado con exito!!")

def buscar_usuario():
    nombre = input("Ingrese usuario a buscar: ").lower()

    if nombre in usuarios:
        print("El sexo del usuario es:", usuarios[nombre]["sexo"], "y la contraseña es:", usuarios[nombre]["contrasena"])
    else:
        print("El usuario no se encuentra.")

def eliminar_usuario():
    nombre = input("Ingrese usuario a buscar: ")

    if nombre in usuarios:
        del usuarios[nombre]
        print("Usuario eliminado con éxito!")
    else:
        print("No se pudo eliminar usuario!")

def mostrar_menu():
    print("MENU PRINCIPAL")
    print("1.- Ingresar usuario.")
    print("2.- Buscar usuario.")
    print("3.- Eliminar usuario.")
    print("4.- Salir.")

def main():
    while True:
        mostrar_menu()
        opcion = input("Ingrese opción: ")

        if opcion == "1":
            ingresar_usuario()
        elif opcion == "2":
            buscar_usuario()
        elif opcion == "3":
            eliminar_usuario()
        elif opcion == "4":
            print("Programa terminado...")
            break
        else:
            print("Debe ingresar una opción válida!!")

main()





