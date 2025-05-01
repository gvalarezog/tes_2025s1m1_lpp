

lista_frutas = ["naranja",'manzana', 'limon',"pera"]
# print(lista_frutas)
#
# print(lista_frutas[2])
# #naranja
# print(lista_frutas[0])
#
# print(len(lista_frutas))

#permite cambiar la lista original
print(lista_frutas)

lista_frutas[1] = 'piña'
print(lista_frutas)

lista_frutas[3] = "piña"
print(lista_frutas)
print(lista_frutas[0])


lista1 = []
print(lista1)
print(len(lista1))

lista1 = ['abc', 123, 125.20, True, 'abc', 369,False, 'zaq', 25.36]
print(lista1)
print(type(lista1[0]))
print(type(lista1[1]))
print(type(lista1[2]))
print(type(lista1[3]))
print(len(lista1))

lista2 = list(('abc', True, '123'))
print(lista2)
print('*'.center(80, '*'))
#acceso a los elmentos con rangos e indices negativos
lista_frutas = ["naranja",'manzana', 'limon',"pera", 'abc', 123, 125.20, True, 'abc', 369,False, 'zaq', 25.36, 'abc', 123, 125.20, True, 'abc', 369,False, 'zaq', 25.36]
print(lista_frutas)
print(lista_frutas[21])
print(lista_frutas[-1])
print(len(lista_frutas))
print(lista_frutas[len(lista_frutas)-1])
# print(lista_frutas[22])
print(lista_frutas[-2])

print(lista_frutas[0:5])
print(lista_frutas[0:-1])
print(lista_frutas[0:])
print(lista_frutas[7:-1])
print(lista_frutas[7:-6])


lista_frutas = ["naranja",'manzana', 'limon',"pera"]
if 'piña' in lista_frutas:
    print('El piña si esta dentro de la lista')
else:
    print('La piña no esta dentro de la lista')

cedulas = [5,8,9,4,2,6,7,4,]
if 0 in cedulas:
    print('Si esta')
else:
    print('No esta')

print('*'.center(80, '*'))
lista_frutas = ["naranja",'manzana', 'limon',"pera"]
print(lista_frutas)
lista_frutas.append('piña')
print(lista_frutas)
lista_frutas.insert(1,'uva')
print(lista_frutas)

lista_frutas.remove('limon')
print(lista_frutas)
# lista_frutas.remove('durazno')
lista_frutas.pop(0)
print(lista_frutas)
lista_frutas.pop(-1)
print(lista_frutas)
lista_frutas.pop()
print(lista_frutas)

x = 5
print(x)

# del lista_frutas
print(lista_frutas)
lista_frutas.clear()
print(lista_frutas)
print('*'.center(80, '*'))
lista_frutas = ["naranja",'manzana', 'limon',"pera"]
print(lista_frutas)
for fruta in lista_frutas:
    print(fruta.capitalize())
    print(fruta.upper())
print('*'.center(80, '*'))
i = 0
while i < len(lista_frutas):
    print(lista_frutas[i].capitalize())
    print(lista_frutas[i].upper())
    i += 1

print('*'.center(80, '*'))
lista_frutas = ["naranja",'manzana', 'limon',"pera"]
print(lista_frutas)
lista_frutas.sort()
print(lista_frutas)
lista_frutas.sort(reverse=True)
print(lista_frutas)
print('*'.center(80, '*'))
lista_frutas = ["naranja",'manzana', 'limon',"pera"]
print(lista_frutas)
lista_frutas.reverse()
print(lista_frutas)

print(lista_frutas.count('limon'))
lista_frutas.append('manzana')
print(lista_frutas.count('manzana'))