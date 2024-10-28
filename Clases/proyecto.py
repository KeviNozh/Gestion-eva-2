class Proyecto:
    def __init__(self, nombre, descripcion, fecha_inicio):
        self.nombre = nombre
        self.descripcion = descripcion
        self.fecha_inicio = fecha_inicio
        self.empleados = []

    def asignar_empleado(self, empleado):
        self.empleados.append(empleado)

    def obtener_info(self):
        return f"Proyecto: {self.nombre}, Descripción: {self.descripcion}, Fecha de Inicio: {self.fecha_inicio}"
