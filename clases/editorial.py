from Libro import Libro

class Editorial():
    def __init__(self, rut_editorial, telefono, correo, direccion, isbn_libro):
        super.__init__(isbn_libro)
        self.rut_editorial = rut_editorial
        self.telefono = telefono
        self.correo = correo
        self.direccion = direccion



