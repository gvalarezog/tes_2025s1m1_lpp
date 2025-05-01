class Persona:
    def __init__(self, cedula, nombre, apellido, edad=None):
        self._cedula = cedula
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad

    def __str__(self):
        return f'Persona: {self.__dict__.__str__()}'

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, edad):
        self._edad = edad

    @property
    def cedula(self):
        return self._cedula

    # @cedula.setter
    # def cedula(self, cedula):
    #     self._cedula = cedula


if __name__ == "__main__":
    persona1 = Persona(nombre='Luis', apellido='Perez', edad=20, cedula='0123456789')
    # print(f'{persona1._nombre} {persona1._apellido} y su edad: {persona1._edad}')
    # print(f'{persona1._apellido} {persona1._nombre} y su edad: {persona1._edad}')
    print(persona1)

    print(persona1.nombre)
    print(persona1.apellido)
    print(persona1.edad)
    print(f'{persona1.nombre} {persona1.apellido} y su edad: {persona1.edad}')
    persona1.edad = 21
    persona1.nombre = 'Lalo'
    persona1.apellido = 'Paz'
    persona1.cedula = '9876543210'
    print(persona1)
    # persona2 =  Persona(nombre='Maria', apellido='Paza', cedula='0321456987')
    # print(persona2)
