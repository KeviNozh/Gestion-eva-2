from DAL.obtener_usuario import ObtenerUsuario

class AutenticarUsuario:
    def __init__(self, usuario, contrasena):
        self.usuario = usuario
        self.contrasena = contrasena

    def ejecutar(self):
        """Autentica al usuario verificando su contraseña"""
        usuario_data = ObtenerUsuario(self.usuario).ejecutar()
        if usuario_data and usuario_data[2] == self.contrasena:
            print(f"Usuario '{self.usuario}' autenticado correctamente.")
            return True
        print(f"Error de autenticación para el usuario '{self.usuario}'.")
        return False
