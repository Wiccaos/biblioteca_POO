from datetime import date

class Persona:
    def __init__(self, rut, nombre, apellido, direccion, telefono, correo, fecha_nacimiento):
        """Constructor de la clase Persona"""
        self.rut = rut
        self.nombre = nombre
        self.apellido = apellido
        self.direccion = direccion
        self.telefono = telefono
        self.correo = correo
        self.fecha_nacimiento = fecha_nacimiento

    def calcular_edad(self):
            """Metodo para calcular la edad de la persona"""
            hoy = date.today()
            if self.fecha_nacimiento.month > hoy.month:
                edad = hoy.year - self.fecha_nacimiento.year - 1
            elif self.fecha_nacimiento.month == hoy.month and self.fecha_nacimiento.day > hoy.day:
                edad = hoy.year - self.fecha_nacimiento.year - 1
            else:
                edad = hoy.year - self.fecha_nacimiento.year
            return edad
