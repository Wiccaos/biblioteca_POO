#Importamos la clase Libro para la herencia
import Libro

class Detalle_libro(Libro):
    """Clase de Detalle del libro, que muestra la descripción del libro, la clase tiene herencia de Libro"""
    def __init__(self, codigo_dl, categoria, isbn_libro, run_editorial):
        #El atributo isbn_libro es herencia del atributo Libro
        super().__init__.Libro(isbn_libro)
        self.codigo_dl = codigo_dl
        self.categoria = categoria
        self.run_editorial = run_editorial
