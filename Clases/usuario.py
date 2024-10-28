class Usuario:
    def __init__(self, nombre, email, telefono):
        self.nombre = nombre
        self.email = email
        self.telefono = telefono

    def obtener_info(self):
        return f"Usuario: {self.nombre}, Email: {self.email}, Teléfono: {self.telefono}"
