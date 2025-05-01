

diccionario_frutas = {"uva": 5, "naranja": 6, 'piña': 1}
print(diccionario_frutas)

print(diccionario_frutas["naranja"])
print(diccionario_frutas.fromkeys("naranja"))

diccionario_frutas['manzana'] = 7

print(diccionario_frutas)

for key, value in diccionario_frutas.items():
    print(f'Tengo {value} {key}')

for llave in diccionario_frutas.keys():
    print(llave)

for valor in diccionario_frutas.values():
    print(valor)

for llave in diccionario_frutas.keys():
    print(diccionario_frutas[llave])

inventario = 0
for valor in diccionario_frutas.values():
    inventario += valor

print(inventario)

diccionario_frutas.pop('naranja')
print(diccionario_frutas)