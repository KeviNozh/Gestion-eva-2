from DAL.crear_usuario import CrearUsuario as CrearUsuarioDAL

class CrearUsuario:
    def __init__(self, usuario, contrasena):
        self.usuario = usuario
        self.contrasena = contrasena

    def ejecutar(self):
        """Crea un usuario en la base de datos llamando a la función DAL"""
        nuevo_usuario = CrearUsuarioDAL(self.usuario, self.contrasena)
        nuevo_usuario.ejecutar()
        print(f"Usuario '{self.usuario}' creado con éxito.")
