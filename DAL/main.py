from crear_usuario import CrearUsuario
from obtener_usuario import ObtenerUsuario
from actualizar_usuario import ActualizarUsuario
from eliminar_usuario import EliminarUsuario
from crear_tabla_usuarios import CrearTablaUsuarios
from listar_usuarios import ListarUsuarios
from conexion import ConexionDB

from conexion import ConexionDB

def main():
    conexion = ConexionDB().conectar()
    if conexion:
        print("Conexión establecida con éxito.")
    else:
        print("Error en la conexión.")

    ConexionDB().cerrar()

if __name__ == "__main__":
    main()
