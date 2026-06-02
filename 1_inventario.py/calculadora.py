def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

print("Calculadora simple")
num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))

print("Suma:", sumar(num1, num2))
print("Resta:", restar(num1, num2))


def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def pedir_numero(mensaje):
    while True:
        try:
            numero = int(input(mensaje))
            return numero
        except ValueError:
            print("Error: debes ingresar un número válido.")

print("Calculadora simple con validación")

num1 = pedir_numero("Ingresa el primer número: ")
num2 = pedir_numero("Ingresa el segundo número: ")

print("Suma:", sumar(num1, num2))
print("Resta:", restar(num1, num2))