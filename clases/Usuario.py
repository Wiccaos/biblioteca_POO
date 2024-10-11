from Persona import Persona

class Usuario(Persona):
    """Clase que representa un usuario"""
    def __init__(self, rut, nombre, apellido, direccion, telefono, correo, fecha_nacimiento, id_usuario):
        """Constructor de la clase usuario"""
        super().__init__(rut, nombre, apellido, direccion, telefono, correo, fecha_nacimiento)
        self.id_usuario = id_usuario

    #Metodos
    def solicitar_prestamo(self):
        """Metodo para solicitar un prestamo."""
        pass
    def devolver_libro(self):
        """Metodo para devolver un libro."""
        pass
