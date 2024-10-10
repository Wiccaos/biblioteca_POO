#Importamos la clase necesarias para la herencia
import editorial

class Libro(editorial):
    def __init__(self, titulo_libro, id_autor, isbn_libro, run_editorial):
        #el atributo run_editorial es herencia de la clase libro y editorial
        super().__init__.editorial(run_editorial) = run_editorial
        self.isbn_libro = isbn_libro
        self.titulo_libro = titulo_libro
        self.id_autor = id_autor