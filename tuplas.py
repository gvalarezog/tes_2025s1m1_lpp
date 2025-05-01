from listas import lista_frutas

tupla_frutas = ('naranja', 'pera', 'uva', 'manzana')
print(tupla_frutas)

print(tupla_frutas[1])

# tupla_frutas[1] = 'manzana'
# print(tupla_frutas)

# tupla_frutas.append('manzana')
# tupla_frutas.insert(1,'manzana')
# tupla_frutas.pop()
# tupla_frutas.remove('uva')
# print(tupla_frutas)

for fruta in tupla_frutas:
    print(fruta.upper())

print(tupla_frutas[-1])
print('*'.center(80,'*'))
print(tupla_frutas)
# tupla_frutas.reverse()
# print(tupla_frutas)

print('*'.center(80,'*'))
lista_frutas = list(tupla_frutas)
print(lista_frutas)
print(tupla_frutas)
lista_frutas.append('piña')
print(lista_frutas)
print(tupla_frutas)
tupla_frutas = tuple(lista_frutas)
print(lista_frutas)
print(tupla_frutas)
print(type(tupla_frutas))