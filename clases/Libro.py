from editorial import Editorial
from detalle_libro import DetalleLibro
from autor import Autor

class Libro(Editorial, DetalleLibro, Autor):
    def __init__(self, isbn_libro, titulo, seudonimo_autor, disponibilidad, id_autor, rut_editorial, id_detalle):
        Editorial.__init__(self, rut_editorial)
        DetalleLibro.__init__(self, id_detalle)
        Autor.__init__(self, seudonimo_autor, id_autor)
        self.isbn_libro = isbn_libro
        self.titulo = titulo
        self.disponibilidad = disponibilidad
