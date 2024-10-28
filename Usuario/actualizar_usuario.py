from DAL.actualizar_usuario import ActualizarUsuario as ActualizarUsuarioDAL

class ActualizarUsuario:
    def __init__(self, usuario, nueva_contrasena):
        self.usuario = usuario
        self.nueva_contrasena = nueva_contrasena

    def ejecutar(self):
        """Actualiza la contraseña del usuario en la base de datos"""
        actualizar = ActualizarUsuarioDAL(self.usuario, self.nueva_contrasena)
        actualizar.ejecutar()
        print(f"Contraseña de '{self.usuario}' actualizada con éxito.")
