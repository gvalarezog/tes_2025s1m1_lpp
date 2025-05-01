
mes = int(input("Ingrese el numero de mes del año: "))

if mes == 1 or mes == 2 or mes == 12:
    print('Invierno')
elif mes == 3 or mes == 4 or mes == 5:
    print('Primavera')
elif mes == 6 or mes == 7 or mes == 8:
    print('verano')
elif mes == 9 or mes == 10 or mes == 11:
    print('Otoño')
else:
    print('El mes ingresado no es valido')