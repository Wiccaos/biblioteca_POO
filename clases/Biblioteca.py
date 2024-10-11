class biblioteca():
    """Clase que representa una biblioteca."""
    def __init__(self, rut_biblioteca, nombre, direccion, telefono):
        """Constructor de la clase biblioteca."""
        self.nombre = nombre
        self.rut_biblioteca = rut_biblioteca
        self.direccion = direccion
        self.telefono = telefono
