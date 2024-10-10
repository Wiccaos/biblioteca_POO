#Importamos las clases que son necesarias para la herencia
from Libro import Libro
from Usuario import Usuario
from Bibliotecario import Bibliotecario
from datetime import datetime

class Prestamo(Libro, Usuario, Bibliotecario):
    def __init__(self, fecha_prestamo, fecha_devolucion, isbn_libro, fecha_dev_real, multa, id_usuario, id_bibliotecario):
        self.fecha_prestamo = fecha_prestamo
        self.fecha_devolucion = fecha_devolucion
        Libro.__init__(self, isbn_libro)
        Usuario.__init__(self, id_usuario)
        Bibliotecario.__init__(self, id_bibliotecario)
    
    #Metodos
    def calc_fecha_dev():
        #Calcula la fecha de devolucion ideal
        pass

    def calcular_multa():
        #Calcula la multa que debe pagar el usuario si es que no devolvió el libro a tiempo
        pass
