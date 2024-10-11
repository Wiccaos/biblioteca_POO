#Importamos la clase Libro para usar la herencia
from Libro import Libro

class Editorial(Libro):
    """Clase que representa una Editorial"""
    def __init__(self, rut_editorial, telefono, correo, direccion, isbn_libro):
        """Constructor de la clase Editorial, Llama al constructor de la clase Libro
         y fija los valores de los atributos propios de la clase."""
        super.__init__(isbn_libro)
        self.rut_editorial = rut_editorial
        self.telefono = telefono
        self.correo = correo
        self.direccion = direccion



