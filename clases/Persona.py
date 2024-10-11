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
            edad = hoy.year - self.fecha_nacimiento.year - ((hoy.month, hoy.day) < (self.fecha_nacimiento.month, self.fecha_nacimiento.day))
            return edad
    
# Ejemplo de uso:
persona1 = Persona("12345678-9", "Juan", "Pérez", "Calle 123", "123456789", "juan@example.com", date(1990, 1, 1))
print(persona1.calcular_edad())
