#Importamos las clases que son necesarias para la herencia
from Libro import Libro
from Usuario import Usuario
from Bibliotecario import Bibliotecario
from datetime import datetime

class Prestamo(Libro, Usuario, Bibliotecario):
    def __init__(self, fecha_prestamo, fecha_devolucion, isbn_libro, fecha_dev_real, multa, id_usuario, id_bibliotecario):
        self.fecha_prestamo = fecha_prestamo
        self.fecha_devolucion = fecha_devolucion
        Libro.__init__(isbn_libro)
        Usuario.__init__(id_usuario)
        Bibliotecario.__init__(id_bibliotecario)
    
    #Metodos
    def calc_fecha_dev():
        #Calcula la fecha de devolucion ideal
        pass

    def calcular_multa():
        #Calcula la multa que debe pagar el usuario si es que no devolvió el libro a tiempo
        #Si la fecha de devolucion real es mayor a la fecha de devolucion ideal, entonces
        #se calcula la multa que debe pagar el usuario
        pass
