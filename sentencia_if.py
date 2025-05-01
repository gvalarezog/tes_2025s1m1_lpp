

# #condicion si (if)
# condicion = False
#
# if condicion:
#     #ejeucto esta seccion
#     print("La condicion es verdadera")
# else:
#     print("La condicion no es verdadera")

edad = int(input("Ingrese su edad: "))

# condicion = edad >=18
#
# if edad >=18:
#     print("Es mayor edad")
#
# else:
#     print("Es menor de edad")


#quiero conocer el rango de la edad del usuario que ingreso, por ejemplo si esta dentro de los 20 a 30 y 30 a 40
if edad >= 20 and edad <30:
    print("Esta dentro de los 20's")
elif edad >=30 and edad < 40:
    print("Esta dentro de los 30's")
else:
    print("No es parte de los 20's ni 30's")