class Vehiculo:
    def __init__(self, marca, modelo, año, cilindraje=0, tipo="Desconocido", color="Desconocido", precio=0, pais_origen="Desconocido", placa="Desconocida", no_chasis="Desconocido", caja="Desconocida", combustible="Desconocido", seguridad="Desconocida", transmision="Desconocida", kilometraje=0):
        """Inicializa las propiedades del vehículo con atributos obligatorios y opcionales."""
        self._marca = marca
        self._modelo = modelo
        self._año = año
        self._cilindraje = cilindraje
        self._tipo = tipo
        self._color = color
        self._precio = precio
        self._pais_origen = pais_origen
        self._placa = placa
        self._no_chasis = no_chasis
        self._caja = caja
        self._combustible = combustible
        self._seguridad = seguridad
        self._transmision = transmision
        self._kilometraje = kilometraje
        self._velocidad_actual = 0

    # Encapsulación de atributos usando @property y @setter
    @property
    def marca(self):
        return self._marca

    @marca.setter
    def marca(self, valor):
        self._marca = valor

    @property
    def modelo(self):
        return self._modelo

    @modelo.setter
    def modelo(self, valor):
        self._modelo = valor

    @property
    def año(self):
        return self._año

    @año.setter
    def año(self, valor):
        self._año = valor

    # Métodos para manipular la velocidad
    def acelerar(self, cantidad):
        """Aumenta la velocidad del vehículo."""
        self._velocidad_actual += cantidad
        print(f"El vehículo ha acelerado. Velocidad actual: {self._velocidad_actual} km/h")

    def frenar(self, cantidad):
        """Reduce la velocidad del vehículo, pero no por debajo de 0."""
        self._velocidad_actual = max(0, self._velocidad_actual - cantidad)
        print(f"El vehículo ha frenado. Velocidad actual: {self._velocidad_actual} km/h")

    # Método para mostrar toda la información
    def mostrar_info(self):
        """Muestra toda la información del vehículo."""
        print(self.__str__())  # Utiliza el método __str__

    def __str__(self):
        """Devuelve una representación en cadena de los atributos del vehículo."""
        atributos = "\n".join([f"{key[1:]}: {value}" for key, value in self.__dict__.items()])
        return f"Información del Vehículo:\n{atributos}"


if __name__ == "__main__":
    # Crear un objeto Vehiculo con solo los atributos obligatorios
    mi_vehiculo = Vehiculo(
        marca="Toyota",
        modelo="Corolla",
        año=2020
    )

    # Probar los métodos
    print(mi_vehiculo)  # Muestra la información del vehículo con __str__
    mi_vehiculo.acelerar(40)  # Aumenta la velocidad
    mi_vehiculo.frenar(20)    # Reduce la velocidad
    #se agrega este comentario