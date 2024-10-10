from Persona import Persona

class Usuario(Persona):
    def __init__(self, rut, nombre, apellido, direccion, telefono, correo, fecha_nacimiento, id_usuario):
        super().__init__(rut, nombre, apellido, direccion, telefono, correo, fecha_nacimiento)
        self.id_usuario = id_usuario

    #Metodos
    def solicitar_prestamo():
        pass
    def devolver_libro():
        pass
