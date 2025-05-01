# frutas = ['naranja', 'manzana', 'uva']
#
# print(frutas)
# for fruta in frutas:
#     print(fruta)

# contador = 0
# impares = 0
# for numero in range(1, 51):
#     if numero % 2 == 0:
#         contador = contador + 1
#     else:
#         impares = impares + 1
# print(contador)
# print(impares)


numero_ingresado = int(input('Ingresa un numero: '))

contador = 0
for numero in range(2, numero_ingresado):
    if numero_ingresado % numero == 0:
        contador = contador + 1

if contador == 0:
    print(f'El numero {numero_ingresado} es primo')
else:
    print(f'El numero {numero_ingresado} no es primo')



