from base_datos.funciones_data import *

def listar_campers_inscritos():
    limpiar_pantalla()
    print("Campers Inscritos:")
    for camper in lista_campers:
        if 'estado' in camper and camper['estado'] == "Inscrito":
            print(f"Nombre: {camper['nombre']} {camper['apellido']}")
            print(f"Identificación: {camper['identificacion']}")
            print("------------------------")

def campers_aprobados():
    limpiar_pantalla()
    for camper in lista_campers:
        if 'prueba_inicial' in camper and camper['prueba_inicial'] >= 60:
            print(f"Nombre: {camper['nombre']} {camper['apellido']}")
            print(f"Identificación: {camper['identificacion']}")
            print("------------------------")

def listar_trainers():
    limpiar_pantalla()
    print("Lista de Trainers:")
    for trainer in lista_trainers:
        print(f"Nombre: {trainer['nombre']} {trainer['apellido']}")
        print(f"Especialidad: {trainer['especialidad']}")
        print(f"Horario Disponible: {trainer['horario_disponible']}")
        print(f"Rutas Asignadas: {', '.join(trainer['rutas_asignadas'])}")
        print(f"Aula Asignada: {trainer['aula_asignada']}")
        print("------------------------")

def reprobados_aprobados_modulos():
    # Contadores para los resultados
    aprobados = 0
    reprobados_trabajo_clase = 0
    reprobados_evaluacion_filtro = 0
    reprobados_trabajo_practico = 0

    # Iterar sobre la lista de campers
    for camper in lista_campers:
        # Verificar si la nota de trabajo_clase es menor o igual a 60
        if camper.get('nota_trabajo_clase', 90) <= 60:
            reprobados_trabajo_clase += 1

        # Verificar si la nota de evaluacion_filtro es menor o igual a 60
        if camper.get('nota_evaluacion_filtro', 90) <= 60:
            reprobados_evaluacion_filtro += 1

        # Verificar si la nota de trabajo_practico es menor o igual a 60
        if camper.get('nota_trabajo_practico', 90) <= 60:
            reprobados_trabajo_practico += 1

        # Verificar si el camper perdió al menos uno de los módulos
        if camper.get('nota_trabajo_clase', 90) <= 60 or camper.get('nota_evaluacion_filtro', 90) <= 60 or camper.get('nota_trabajo_practico', 90) <= 60:
            camper['perdio_modulo'] = True
        else:
            camper['perdio_modulo'] = False
            aprobados += 1

    # Mostrar resultados
    print("Resultados de módulos:")
    print(f"Aprobados: {aprobados}")
    print(f"Reprobados Trabajo Clase: {reprobados_trabajo_clase}")
    print(f"Reprobados Evaluacion Filtro: {reprobados_evaluacion_filtro}")
    print(f"Reprobados Trabajo Practico: {reprobados_trabajo_practico}")

    # Actualizar el archivo JSON
    guardar_json()
