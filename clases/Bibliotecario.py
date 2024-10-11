#importamos la Clase persona para la herencia
from Persona import Persona

class Bibliotecario(Persona):
    def __init__(self, rut, nombre, apellido, direccion, telefono, correo, fecha_nacimiento, id_bibliotecario):
        """Constructor de la clase Bibliotecario. Llama al constructor de la clase
        padre y fija los valores de los atributos propios de la clase."""
        super().__init__(rut, nombre, apellido, direccion, telefono, correo, fecha_nacimiento)
        self.id_bibliotecario = id_bibliotecario
        
    #Metodos
    def agregar_libro(self):
        """Agrega un Libro a la base de datos."""
        pass

    def eliminar_libro(self):
        """Elimina un Libro de la base de datos."""
        pass

    def registrar_prestamo(self):
        """Registra un prestamo de un libro."""
        pass

    def registrar_devolucion(self):
        """Registra la devolución de un libro."""
        pass

    def registrar_usuario(self):
        """Registra un usuario."""
        pass
    