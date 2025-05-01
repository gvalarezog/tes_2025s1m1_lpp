#Escribir un programa que almacene la cadena de caracteres contraseña en una variable,
# pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.


password = "Secreto"

# while True:
#     user_passd = input("Ingrese la contraseña: ")
#
#     if user_passd == password:
#         print(f'Contraseña correcta')
#         print(f'Acceso concedido')
#         break
#     else:
#         print(f'Contraseña incorrecta')
#         print(f'Intente de nuevo.')



MAX_INTENTOS = 3

bandera_salir = False
contador_intentos = 0
while not bandera_salir and contador_intentos < MAX_INTENTOS:
    user_passd = input("Ingrese la contraseña: ")
    contador_intentos += 1 # contador_intentos = contador_intentos + 1
    if user_passd == password:
        print(f'Contraseña correcta')
        print(f'Acceso concedido')
        bandera_salir = True
    else:
        print(f'Contraseña incorrecta')
        print(f'Intente de nuevo.')
        bandera_salir = False
    # if contador_intentos >= MAX_INTENTOS:
    #     bandera_salir = True
    #     print(f"Numero de intentos fallidos: {contador_intentos}")