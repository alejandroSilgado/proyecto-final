from utilidades.funciones import *

def menu_principal():
    print("----------- Menú Principal-----------")
    print("1. Configuracion Campers")
    print("2. Configuracion Rutas")
    print("3. Configuracion Aulas")
    print("4. Configuracion Trainers")
    print("5. Configuracion Matriculas")
    print("6. Configuracion Reportes") 
    print("7. Salir del programa")      
    op=verificar_opcion("Opcion: ",1,7)
    return op

def menu_campers():
    print("----------- Menú Campers-----------")
    print("1. Crear campers")
    print("2. Listar campers")
    print("3. Ingresar nota de los modulos")
    print("4. Ingresar nota de la prueba inicial")
    print("5. Definir ruta campers")
    print("6. Modificar campers")
    print("7. Salir")
    op=verificar_opcion("Opcion: ",1,7)
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
    limpiar_pantalla()
    print("----------- Menú De Seleccion De Ruta -----------")
    print("1. Ruta NodeJS")
    print("2. Ruta Java")
    print("3. Ruta NetCore")
    print("4. Salir")
    op=verificar_opcion("Opcion: ",1,4)
    return op

def menu_trainers():
    print("----------- Menú Trainers-----------")
    print("1. Crear trainers")
    print("2. Buscar trainers")
    print("3. Modificar trainers")
    print("4. Listar trainers")
    print("5. Agregar trainer a una ruta")
    print("6. Agregar trainer a una area")
    print("7. Salir")

    op=verificar_opcion("Opcion: ",1,7)
    return op

def menu_matriculas():
    print("----------- Menú Matriculas-----------")
    print("1. Crear Matriculas")
    print("2. Listar Matriculas")
    print("3. Modificar Matriculas")
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
    print("1. Listar los campers inscritos")
    print("2. Listar los campers que aprobaron el examen inicial")
    print("3. Listar los entrenadores trabajando")
    print("4. Mostrar cuantos campers perdieron y aprobaron cada uno de los modulos")
    print("5. Salir")

    op=verificar_opcion("Opcion: ",1,5)
    return op


