#Importamos las clases que son necesarias para la herencia
from Libro import Libro
from Usuario import Usuario
from Bibliotecario import Bibliotecario
from datetime import datetime

class Prestamo(Libro, Usuario, Bibliotecario):
    """Clase que representa un prestamo de un libro."""
    def __init__(self, fecha_prestamo, fecha_devolucion, libro, usuario, bibliotecario, fecha_dev_real, multa):
        """Constructor de la clase prestamo"""
        Libro.__init__(self, libro.isbn)
        Usuario.__init__(self, usuario.rut, usuario.nombre, usuario.apellido, usuario.correo, usuario.fecha_nacimiento)
        Bibliotecario.__init__(self, bibliotecario.rut, bibliotecario.nombre, bibliotecario.apellido, bibliotecario.correo, bibliotecario.fecha_nacimiento)
        self.fecha_prestamo = fecha_prestamo
        self.fecha_devolucion = fecha_devolucion
        self.fecha_dev_real = fecha_dev_real
        self.multa = multa
        self.id_usuario = usuario.id
        self.id_bibliotecario = bibliotecario.id

    def calc_fecha_dev(self):
        """Calcula la fecha de devolucion ideal del libro"""
        self.fecha_devolucion = self.fecha_prestamo + datetime.timedelta(days=30)

    def calcular_multa(self):
        """Calcula la multa que debe pagar el usuario si es que no devolvió el libro a tiempo"""
        if self.fecha_dev_real > self.fecha_devolucion:
            dias_atraso = (self.fecha_dev_real - self.fecha_devolucion).days
            multa_por_dia = 500
            self.multa = dias_atraso * multa_por_dia
        else:
            self.multa = 0

