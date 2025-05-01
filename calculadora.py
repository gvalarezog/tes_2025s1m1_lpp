
def presentar_menu():
    print(f'1) Sumar')
    print(f'2) Restar')
    print(f'3) Multiplicar')
    print(f'4) Dividir')
    print(f'9) Salir')

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a / b

def ingresar_operador():
    valor = float(input('Ingresar el valor: '))
    return valor



presentar_menu()

opcion = int(input("Escoja la operación deseada: "))

while opcion != 9:
    a = ingresar_operador()
    b = ingresar_operador()
    if opcion == 1:
        print(f'El resultado es: {sumar(a, b)}')
    elif opcion == 2:
        print(f'El resultado es: {restar(a, b)}')
    elif opcion == 3:
        print(f'El resultado es: {a * b}')
    elif opcion == 4:
        print(f'El resultado es: {a / b}')
    elif opcion == 9:
        print(f'Salir')
    else:
        print('Opcion invalida')
    opcion = int(input("Escoge la operación deseada: "))

