#Importar los objetos necesarios para la herencia
from editorial import Editorial
from detalle_libro import DetalleLibro
from autor import Autor

class Libro(Editorial, DetalleLibro, Autor):
    """Clase que representa un Libro"""
    def __init__(self, isbn_libro, titulo, seudonimo_autor, disponibilidad, id_autor, rut_editorial, id_detalle):
        """Constructor de la clase Libro. Llama al constructor de las clases
        superiores y fija los valores de los atributos propios de la
        clase."""
        Editorial.__init__(self, rut_editorial)
        DetalleLibro.__init__(self, id_detalle)
        Autor.__init__(self, seudonimo_autor, id_autor)
        self.isbn_libro = isbn_libro
        self.titulo = titulo
        self.disponibilidad = disponibilidad
    
