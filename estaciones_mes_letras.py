
ingreso_mes = input("Ingrese el mes: ")
mes = ingreso_mes.lower().strip()


if mes == 'diciembre' or mes == 'enero' or mes == 'febrero':
    print("Invierno")
elif mes == 'marzo' or mes == 'abril' or mes == 'mayo':
    print("Primavera")
elif mes == 'junio' or mes == 'julio' or mes == 'agosto':
    print("Verano")
elif mes == 'septiembre' or mes == 'octubre' or mes == 'noviembre':
    print("Otoño")
else:
    print("El mes no es valido")