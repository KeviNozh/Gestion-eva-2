import mysql.connector

class ConexionDB:
    def __init__(self): 
        self.host = "127.0.0.1"
        self.user = "tu_usuario_mysql"          
        self.password = "tu_contraseña"    
        self.database = "gestion"               
        self.conexion = 3306

    def conectar(self):
        try:
            self.conexion = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            print("Conexión exitosa a la base de datos.")
            return self.conexion
        except mysql.connector.Error as e:
            print(f"Error al conectar a MySQL: {e}")
            return None

    def cerrar(self):
        if self.conexion:
            self.conexion.close()
            print("Conexión cerrada.")
