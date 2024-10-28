from .conexion import ConexionDB

class ListarUsuarios:
    def ejecutar(self):
        conexion = ConexionDB().conectar()
        if conexion:
            cursor = conexion.cursor()
            query = "SELECT * FROM usuarios"
            cursor.execute(query)
            usuarios = cursor.fetchall()
            cursor.close()
            conexion.close()
            return usuarios
        return []
