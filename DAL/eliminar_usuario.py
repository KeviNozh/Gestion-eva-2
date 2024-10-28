from .conexion import ConexionDB

class EliminarUsuario:
    def __init__(self, usuario):
        self.usuario = usuario

    def ejecutar(self):
        conexion = ConexionDB().conectar()
        if conexion:
            cursor = conexion.cursor()
            query = "DELETE FROM usuarios WHERE usuario = %s"
            cursor.execute(query, (self.usuario,))
            conexion.commit()
            cursor.close()
            conexion.close()

