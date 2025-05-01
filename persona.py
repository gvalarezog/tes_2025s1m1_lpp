class Persona:
    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad


if __name__ == "__main__":
    persona1 = Persona('Luis', 'Perez', 20)
    print(f'{persona1._nombre} {persona1._apellido} y su edad: {persona1._edad}')
    print(f'{persona1._apellido} {persona1._nombre} y su edad: {persona1._edad}')


    persona2 = "Luis Perez 20"
    print(persona2.split(' '))
    print(persona2)

    print(type(persona1))
    print(type(persona2))