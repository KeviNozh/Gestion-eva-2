class Departamento:
    def __init__(self, nombre, gerente):
        self.nombre = nombre
        self.gerente = gerente
        self.empleados = []

    def asignar_empleado(self, empleado):
        self.empleados.append(empleado)

    def obtener_info(self):
        empleados_nombres = [emp.nombre for emp in self.empleados]
        return f"Departamento: {self.nombre}, Gerente: {self.gerente.nombre}, Empleados: {empleados_nombres}"
