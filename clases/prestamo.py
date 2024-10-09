#Importamos las clases que son necesarias para la herencia
import Libro, usuario

class Prestamo(Libro, usuario):
    def __init__(self, isbn_libro, n_usuario, fecha_prestamo, fecha_devolucion, fecha_dev_real):
        #Los atributos isbn y n_usuario son heredados de una clase padre
        super().__init__.Libro(isbn_libro)
        super().__init__.usuario(n_usuario)
        self.fecha_prestamo = fecha_prestamo
        self.fecha_devolucion = fecha_devolucion
        self.fecha_dev_real = fecha_dev_real
    
    def calc_facha_dev(self, fecha_dev_estimada):
        """Método para calcular la fecha de devolución"""
        fecha_dev_estimada = Prestamo.fecha_prestamo + 20
        return fecha_dev_estimada
