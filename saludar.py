

#Escribir una función a la que se le pase una cadena <nombre> y muestre por pantalla el saludo ¡hola <nombre>!.

def saludar(nombre:str, apellido:str, edad:int=None):
    '''
    saludar es una función que pemrite mostrar una cadena de texto salundo
    :param nombre: es el nombre de la persona
    :param apellido: el aplleido de la persona
    :param edad: la edad de la persona es opcional
    :return: el saludo a la persona
    '''
    if edad:
        return f'!Hola {nombre.capitalize() + ' ' + apellido.capitalize()} tu edad es: {edad}!'
    else:
        return f'!Hola {nombre.capitalize() + ' ' + apellido.capitalize()}!'


#no es parte de la función es el llamado a la funcion
print(saludar('MAria', 'Paz', 20))
print(saludar(nombre='luis', apellido='perez'))
print(saludar(apellido='Alonso', nombre='Juan'))
