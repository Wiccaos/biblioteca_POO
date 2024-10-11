#Importamos la clase Libro para la herencia
import Libro

class DetalleLibro(Libro):
    def __init__(self, id_detalle, isbn_libro, categoria, anio_pub, descripcion):
        """Constructor de la clase Libro. Llama al constructor de la clase padre
         y fija los valores de los atributos propios de la clase."""
        super().__init__(isbn_libro)
        self.id_detalle = id_detalle
        self.categoria = categoria
        self.anio_pub = anio_pub
        self.descripcion = descripcion

