from .conexion import ConexionDB

class ActualizarUsuario:
    def __init__(self, usuario, nueva_contrasena):
        self.usuario = usuario
        self.nueva_contrasena = nueva_contrasena

    def ejecutar(self):
        conexion = ConexionDB().conectar()
        if conexion:
            cursor = conexion.cursor()
            query = "UPDATE usuarios SET contrasena = %s WHERE usuario = %s"
            cursor.execute(query, (self.nueva_contrasena, self.usuario))
            conexion.commit()
            cursor.close()
            conexion.close()
