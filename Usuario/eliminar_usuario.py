from DAL.eliminar_usuario import EliminarUsuario as EliminarUsuarioDAL

class EliminarUsuario:
    def __init__(self, usuario):
        self.usuario = usuario

    def ejecutar(self):
        """Elimina un usuario de la base de datos"""
        eliminar = EliminarUsuarioDAL(self.usuario)
        eliminar.ejecutar()
        print(f"Usuario '{self.usuario}' eliminado correctamente.")
