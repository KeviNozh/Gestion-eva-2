from DAL.listar_usuarios import ListarUsuarios as ListarUsuariosDAL

class ListarUsuarios:
    def ejecutar(self):
        """Lista todos los usuarios en la base de datos"""
        usuarios = ListarUsuariosDAL().ejecutar()
        print("Usuarios registrados en el sistema:")
        for usuario in usuarios:
            print(f" - {usuario[1]}")
