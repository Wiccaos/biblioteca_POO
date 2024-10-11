#Importamos la clase Libro para la herenia necesaria
from Libro import Libro

class Autor():
    """ Clase que representa a un autor de un libro """

    def __init__(self, id_autor, seudonimo, nacionalidad, isbn_libro):
        """ Constructor de la clase Autor"""
        super().__init__(isbn_libro)
        self.id_autor = id_autor
        self.seudonimo = seudonimo
        self.nacionalidad = nacionalidad
