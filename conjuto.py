#Conjunto

conjunto_frutas = {'naranja', 'pera', 'uva', 'pera', 'uva'}
print(conjunto_frutas)
print(type(conjunto_frutas))

for fruta in conjunto_frutas:
    print(fruta)

conjunto_frutas.add('piña')
print(conjunto_frutas)

conjunto_frutas.add('uva')
print(conjunto_frutas)

conjunto_frutas.discard('uva ')
print(conjunto_frutas)

conjunto_frutas.add('manzana')
print(conjunto_frutas)

conjunto_frutas.add('manzana')
print(conjunto_frutas)