from utilidades.funciones import *

def menu_principal():
    print("----------- Menú Principal-----------")
    print("1. Campers")
    print("2. Rutas")
    print("3. Aulas")
    print("4. Matriculas")
    print("5. Reportes")
    print("6. Trainers") 
    print("7. Salir")      
    op=verificar_opcion("Opcion: ",1,7)
    return op

def menu_campers():
    print("----------- Menú Campers-----------")
    print("1. Crear campers")
    print("2. Listar campers")
    print("3. Ingresar notas campers")
    print("4. Definir ruta campers")
    print("5. Modificar campers")
    print("6. Salir")
    op=verificar_opcion("Opcion: ",1,6)
    return op
def menu_rutas():
    print("----------- Menú Rutas -----------")
    print("1. Creación de rutas de entrenamiento")
    print("2. Listar ruta de entrenamiento")
    print("3. Borrar ruta de entrenamiento")
    print("4. Salir")
    op=verificar_opcion("Opcion: ",1,4)
    return op
def menu_ruta():
    print("----------- Menú De Seleccion De Ruta Campers-----------")
    print("1. Ruta NodeJS")
    print("2. Ruta Java")
    print("3. Ruta NetCore")
    print("4. Salir")
    op=verificar_opcion("Opcion: ",1,4)
    return op

def menu_trainers():
    print("----------- Menú Trainers-----------")
    print("1. Crear trainer")
    print("2. Buscar trainer")
    print("3. Modificar trainer")
    print("4. Salir")
    op=verificar_opcion("Opcion: ",1,4)
    return op

def menu_matriculas():
    print("----------- Menú Matriculas-----------")
    print("1. Crear Matriculas")
    print("2. Buscar Matriculas")
    print("3. Modificar Matriuclas")
    print("4. Salir")
    op=verificar_opcion("Opcion: ",1,4)
    return op

def menu_aulas():
    print("----------- Menú Aulas-----------")
    print("1. Crear Aulas")
    print("2. Agregar campers a aulas")
    print("3. Listar Aulas activas")
    print("4. Modificar Aulas")
    print("5. Salir")
    op=verificar_opcion("Opcion: ",1,5)
    return op

def menu_reportes():
    print("----------- Menú Reportes-----------")
    print("1. Listar campers estado inscripto")
    print("2. Listar campers aprobaron examen")
    print("3. Listar trainers trabajando en campus")
    print("4. Salir")
    op=verificar_opcion("Opcion: ",1,4)
    return op


