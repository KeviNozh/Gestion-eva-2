class Verificar:
    def __init__(self, contrasena):
        self.contrasena = contrasena

    def verificar_contrasena(self, intento):
        return self.contrasena == intento
