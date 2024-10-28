from .usuario import Usuario

class Empleado(Usuario):
    def __init__(self, nombre, email, telefono, rol):
        super().__init__(nombre, email, telefono)
        self.rol = rol
        self.proyectos = []

    def asignar_proyecto(self, proyecto):
        self.proyectos.append(proyecto)
