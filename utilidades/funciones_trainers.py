from base_datos.funciones_data import *
from menus.menus import *
from utilidades.funciones_rutas import *

def listar_trainers():
    limpiar_pantalla()
    print("Listado de Entrenadores:")
    for trainer in lista_trainers:
        print(f"Nombre: {trainer['nombre']} {trainer['apellido']}")
        print(f"Especialidad: {trainer['especialidad']}")
        print(f"Horario Disponible: {trainer['horario_disponible']}")
        print(f"Rutas Asignadas: {', '.join(trainer['rutas_asignadas'])}")
        print("------------------------")

def agregar_ruta_a_trainer_por_nombre():
    nombre_trainer = input("Ingrese el nombre del entrenador al que desea agregar una ruta: ")

    for trainer in lista_trainers:
        if 'nombre' in trainer and trainer['nombre'] == nombre_trainer:
            ruta_opcion = menu_ruta()

            if ruta_opcion == 1:
                ruta = "Ruta NodeJS"
            elif ruta_opcion == 2:
                ruta = "Ruta Java"
            elif ruta_opcion == 3:
                ruta = "Ruta NetCore"
            elif ruta_opcion == 4:
                print("Operación cancelada. No se ha agregado ninguna ruta.")
                return
            else:
                print("Opción no válida. No se ha agregado ninguna ruta.")
                return

            if 'rutas_asignadas' not in trainer:
                trainer['rutas_asignadas'] = []
            trainer['rutas_asignadas'].append(ruta)
            guardar_trainers_json()
            print(f"Ruta '{ruta}' agregada al entrenador {trainer['nombre']} {trainer['apellido']}.")
            return

    print(f"No se encontró el entrenador con nombre '{nombre_trainer}'.")

def listar_aulas():
    limpiar_pantalla()
    lista_aulas = cargar_areas_json()
    print("Listado de Aulas:")
    for aula in lista_aulas:
        print(f"Nombre del Aula: {aula['nombre_area']}")
    print("------------------------")

def agregar_aula_a_trainer():
    limpiar_pantalla()
    listar_trainers()

    if not lista_trainers:
        print("No hay entrenadores registrados. Registre entrenadores antes de asignar aulas.")
        return

    # Solicitar el nombre del entrenador
    nombre_entrenador = input("Ingrese el nombre del entrenador al que desea asignar un aula: ")

    # Buscar el entrenador por nombre
    trainer_encontrado = None
    for trainer in lista_trainers:
        if 'nombre' in trainer and trainer['nombre'] == nombre_entrenador:
            trainer_encontrado = trainer
            break

    if trainer_encontrado is not None:
        # Mostrar las aulas disponibles
        print("Aulas disponibles:")
        for aula in lista_areas:
            if 'nombre_area' in aula:
                print(f"Nombre: {aula['nombre_area']}, Capacidad Máxima: {aula['capacidad_maxima']}, Campers Inscritos: {len(aula['campers_inscritos'])}")

        # Solicitar el nombre del aula
        nombre_aula = input("Ingrese el nombre del aula que desea asignar al entrenador: ")

        # Verificar si el aula existe
        aula_encontrada = next((aula for aula in lista_areas if 'nombre_area' in aula and aula['nombre_area'] == nombre_aula), None)

        if aula_encontrada is not None:
            # Asignar el aula al entrenador y actualizar la lista
            trainer_encontrado['aula_asignada'] = nombre_aula
            guardar_trainers_json()  # Pasa la lista de entrenadores a la función
            print(f"Aula '{nombre_aula}' asignada al entrenador '{nombre_entrenador}'.")
            
            # Asignar el director del aula y actualizar la lista de aulas
            if 'director_aula' not in aula_encontrada:
                aula_encontrada['director_aula'] = nombre_entrenador
            else:
                aula_encontrada['director_aula'] = nombre_entrenador
            
            guardar_areas_json()  # Actualiza también el archivo de aulas
        else:
            print(f"No se encontró el aula '{nombre_aula}'. Intente de nuevo.")
    else:
        print(f"No se encontró el entrenador '{nombre_entrenador}'. Intente de nuevo.")

def crear_trainer():
    limpiar_pantalla()
    nombre_trainer = input("Ingrese el nombre del entrenador: ")
    apellido_trainer = input("Ingrese el apellido del entreandor: ")
    especialidad = input("Ingrese la especialidad del entrenador: ")
    horario_disponible = input("Ingrese el horario disponible del entrenador: ")

    trainer = {
        'nombre': nombre_trainer,
        'especialidad': especialidad,
        'apellido': apellido_trainer,
        'horario_disponible': horario_disponible,
        'areas_asignadas': [],
        'rutas_asignadas': []
    }

    lista_trainers.append(trainer)
    print(f"Entrenador '{nombre_trainer}' registrado con éxito.")
    guardar_trainers_json()

def buscar_trainer():
    limpiar_pantalla()
    nombre_trainer = input("Ingrese el nombre del entrenador que desea buscar: ")

    trainer_encontrado = None
    for trainer in lista_trainers:
        if 'nombre' in trainer and trainer['nombre'] == nombre_trainer:
            trainer_encontrado = trainer
            break

    if trainer_encontrado is not None:
        print("Información del entrenador:")
        print(f"Nombre: {trainer_encontrado['nombre']}")
        print(f"Apellido: {trainer_encontrado['apellido']}")
        print(f"Especialidad: {trainer_encontrado['especialidad']}")
        print(f"Horario Disponiblse: {trainer_encontrado['horario_disponible']}")
        print(f"Rutas Asignadas: {', '.join(trainer_encontrado['rutas_asignadas'])}")
    else:
        print(f"No se encontró al entrenador '{nombre_trainer}'.")

def modificar_trainers():
    limpiar_pantalla()
    listar_trainers()

    if not lista_trainers:
        print("No hay entrenadores registrados. Registre entrenadores antes de modificar.")
        return

    # Solicitar el nombre del entrenador a modificar
    nombre_entrenador = input("Ingrese el nombre del entrenador que desea modificar: ")

    # Buscar el entrenador por nombre
    trainer_encontrado = None
    for trainer in lista_trainers:
        if 'nombre' in trainer and trainer['nombre'] == nombre_entrenador:
            trainer_encontrado = trainer
            break

    if trainer_encontrado is not None:
        print("Seleccione el valor a modificar:")
        print("1. Nombre")
        print("2. Apellido")
        print("3. Especialidad")
        print("4. Horario Disponible")
        print("5. Rutas Asignadas")
        print("6. Aula Asignada")
        opcion = verificar_opcion("Opción: ", 1, 6)

        if opcion == 1:
            nuevo_nombre = input("Ingrese el nuevo nombre: ")
            trainer_encontrado['nombre'] = nuevo_nombre
        elif opcion == 2:
            nuevo_apellido = input("Ingrese el nuevo apellido: ")
            trainer_encontrado['apellido'] = nuevo_apellido
        elif opcion == 3:
            nueva_especialidad = input("Ingrese la nueva especialidad: ")
            trainer_encontrado['especialidad'] = nueva_especialidad
        elif opcion == 4:
            nuevo_horario = input("Ingrese el nuevo horario disponible: ")
            trainer_encontrado['horario_disponible'] = nuevo_horario
        elif opcion == 5:
            # Modificar las rutas asignadas
            listar_rutas_entrenamiento()
            nuevas_rutas = []
            while True:
                ruta = input("Ingrese una ruta para asignar (o 'fin' para terminar): ")
                if ruta.lower() == 'fin':
                    break
                else:
                    nuevas_rutas.append(ruta)
            trainer_encontrado['rutas_asignadas'] = nuevas_rutas
        elif opcion == 6:
            # Modificar el aula asignada
            listar_areas_entrenamiento()
            nueva_aula = input("Ingrese el nuevo aula asignada: ")
            trainer_encontrado['aula_asignada'] = nueva_aula

        guardar_trainers_json()  # Actualizar el archivo json
        print("Entrenador modificado exitosamente.")
    else:
        print(f"No se encontró el entrenador '{nombre_entrenador}'. Intente de nuevo.")

    limpiar_pantalla()
    if not lista_trainers:
        print("No hay entrenadores registrados. Registre entrenadores antes de modificar.")
        return
    nombre_trainer = input("Ingrese el nombre del entrenador que desea modificar: ")

    trainer_encontrado = None
    for trainer in lista_trainers:
        if 'nombre' in trainer and trainer['nombre'] == nombre_trainer:
            trainer_encontrado = trainer
            break

    if trainer_encontrado is not None:
        print(f"Información actual del entrenador '{nombre_trainer}':")
        print(f"Nombre: {trainer_encontrado['nombre']}")
        print(f"Nombre: {trainer_encontrado['apellido']}")
        print(f"Especialidad: {trainer_encontrado['especialidad']}")
        print(f"Horario Disponible: {trainer_encontrado['horario_disponible']}")
        print(f"Rutas Asignadas: {', '.join(trainer_encontrado['rutas_asignadas'])}")

        nueva_especialidad = input("Ingrese la nueva especialidad del entrenador (o deje en blanco para no modificar): ").strip()
        nuevo_horario_disponible = input("Ingrese el nuevo horario disponible del entrenador (o deje en blanco para no modificar): ").strip()

        if nueva_especialidad:
            trainer_encontrado['especialidad'] = nueva_especialidad
        if nuevo_horario_disponible:
            trainer_encontrado['horario_disponible'] = nuevo_horario_disponible

        guardar_trainers_json()

        print(f"Entrenador '{nombre_trainer}' modificado con éxito.")
    else:
        print(f"No se encontró al entrenador '{nombre_trainer}'. Intente de nuevo.")