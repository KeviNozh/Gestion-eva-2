from crear_usuario import CrearUsuario
from autenticar_usuario import AutenticarUsuario
from actualizar_usuario import ActualizarUsuario
from eliminar_usuario import EliminarUsuario
from listar_usuarios import ListarUsuarios

def main():
    CrearUsuario("usuario_nuevo", "password123").ejecutar()

    autenticar = AutenticarUsuario("usuario_nuevo", "password123")
    if autenticar.ejecutar():
        print("Autenticación exitosa.")
    else:
        print("Error en autenticación.")

    ActualizarUsuario("usuario_nuevo", "nueva_password").ejecutar()

    ListarUsuarios().ejecutar()

    EliminarUsuario("usuario_nuevo").ejecutar()

if __name__ == "__main__":
    main()
