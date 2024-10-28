class Permisos:
    def __init__(self, rol):
        self.rol = rol
        self.permisos = []

    def agregar_permiso(self, permiso):
        self.permisos.append(permiso)

    def obtener_permisos(self):
        return f"Permisos para {self.rol.obtener_rol()}: {', '.join(self.permisos)}"
