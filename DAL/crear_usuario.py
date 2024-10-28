from .conexion import ConexionDB

class CrearUsuario:
    def __init__(self, usuario, contrasena):
        self.usuario = usuario
        self.contrasena = contrasena

    def ejecutar(self):
        conexion = ConexionDB().conectar()
        if conexion:
            cursor = conexion.cursor()
            query = "INSERT INTO usuarios (usuario, contrasena) VALUES (%s, %s)"
            cursor.execute(query, (self.usuario, self.contrasena))
            conexion.commit()
            cursor.close()
            conexion.close()
    