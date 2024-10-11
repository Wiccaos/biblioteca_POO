#importamos la Clase persona para la herencia
from Persona import Persona

class Bibliotecario(Persona):
    def __init__(self, rut, nombre, apellido, direccion, telefono, correo, fecha_nacimiento, id_bibliotecario):
        """Constructor de la clase Bibliotecario. Llama al constructor de la clase
        padre y fija los valores de los atributos propios de la clase."""
        super().__init__(rut, nombre, apellido, direccion, telefono, correo, fecha_nacimiento)
        self.id_bibliotecario = id_bibliotecario
        
    #Metodos
    def agregar_libro():
        # código para agregar un libro a la base de datos
        pass

    def eliminar_libro():
        # código para eliminar un libro de la base de datos
        pass

    def registrar_prestamo():
        # código para registrar un préstamo de un libro
        pass

    def registrar_devolucion():
        # código para registrar la devolución de un libro
        pass

    def registrar_usuario():
        # código para registrar un usuario
        pass
    