from usuario import Usuario
from contrasena import Contrasena
from verificar import Verificar
from departamento import Departamento
from proyecto import Proyecto
from registro_tiempo import RegistroTiempo
from gerente import Gerente
from empleado import Empleado
from rol import Rol
from permisos import Permisos

def main():
    usuario = Usuario("Kevin Torres", "kevin@ejemplo.com", "555-1234")
    contrasena = Contrasena("mi_password")
    print(usuario.obtener_info())

    verificador = Verificar(contrasena.obtener_contrasena())
    print("Autenticación:", "Exitosa" if verificador.verificar_contrasena("mi_password") else "Fallida")

    rol_desarrollador = Rol("Desarrollador")
    permisos = Permisos(rol_desarrollador)
    permisos.agregar_permiso("acceso_proyectos")
    print(permisos.obtener_permisos())

    gerente = Gerente("Laura Pérez", "laura@empresa.com", "555-9876", None)
    departamento = Departamento("Desarrollo", gerente)
    print(departamento.obtener_info())

    proyecto = Proyecto("Proyecto Eco", "Desarrollo sostenible", "2024-01-01")
    empleado = Empleado("Kevin Torres", "kevin@empresa.com", "555-1234", rol_desarrollador)
    proyecto.asignar_empleado(empleado)
    print(proyecto.obtener_info())

if __name__ == "__main__":
    main()
