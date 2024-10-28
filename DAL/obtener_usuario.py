from .conexion import ConexionDB

class ObtenerUsuario:
    def __init__(self, usuario):
        self.usuario = usuario

    def ejecutar(self):
        conexion = ConexionDB().conectar()
        if conexion:
            cursor = conexion.cursor()
            query = "SELECT * FROM usuarios WHERE usuario = %s"
            cursor.execute(query, (self.usuario,))
            resultado = cursor.fetchone()
            cursor.close()
            conexion.close()
            return resultado
        return None
