from .usuario import Usuario

class Gerente(Usuario):
    def __init__(self, nombre, email, telefono, departamento):
        super().__init__(nombre, email, telefono)
        self.departamento = departamento

    def asignar_departamento(self, departamento):
        self.departamento = departamento
