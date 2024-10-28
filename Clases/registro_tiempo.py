class RegistroTiempo:
    def __init__(self, fecha, horas_trabajadas, tareas, usuario, proyecto):
        self.fecha = fecha
        self.horas_trabajadas = horas_trabajadas
        self.tareas = tareas
        self.usuario = usuario
        self.proyecto = proyecto

    def obtener_registro(self):
        return f"{self.fecha}: {self.usuario.nombre} trabajó {self.horas_trabajadas} horas en {self.proyecto.nombre}. Tareas: {self.tareas}"
