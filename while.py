#numeros del 1 al 10 con for

# for numero in range(1,11):
#     print(numero)

# numero = 0
# while numero <= 10:
#     print(numero)
#     numero = numero + 2
# print(f'Salio del While')


#crear el menu de opciones
print(f'1) Sumar')
print(f'2) Restar')
print(f'3) Multiplicar')
print(f'4) Dividir')
print(f'9) Salir')

opcion = int(input("Escoja la operación deseada: "))

while opcion != 9:
    if opcion == 1:
        print(f'Sumar')
    elif opcion == 2:
        print(f'Resta')
    elif opcion == 3:
        print(f'Multiplicar')
    elif opcion == 4:
        print(f'Dividir')
    elif opcion == 9:
        print(f'Salir')
    else:
        print('Opcion invalida')
    opcion = int(input("Escoge la operación deseada: "))
