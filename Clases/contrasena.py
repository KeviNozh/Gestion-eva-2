class Contrasena:
    def __init__(self, valor):
        self.valor = valor

    def obtener_contrasena(self):
        return self.valor

    def actualizar_contrasena(self, nueva_contrasena):
        self.valor = nueva_contrasena
        print("Contraseña actualizada.")
