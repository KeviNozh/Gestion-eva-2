from .conexion import ConexionDB

class CrearTablaUsuarios:
    def ejecutar(self):
        conexion = ConexionDB().conectar()
        if conexion:
            cursor = conexion.cursor()
            query = """
            CREATE TABLE IF NOT EXISTS usuarios (
                id INT AUTO_INCREMENT PRIMARY KEY,
                usuario VARCHAR(50) NOT NULL UNIQUE,
                contrasena VARCHAR(100) NOT NULL
            );
            """
            cursor.execute(query)
            conexion.commit()
            cursor.close()
            conexion.close()
