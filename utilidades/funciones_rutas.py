from base_datos.funciones_data import *
#FUNCIONES AREAS
def agregar_camper_a_area():
    limpiar_pantalla()
    listar_areas_entrenamiento()
    
    if not lista_areas:
        print("No hay áreas de entrenamiento registradas. Registre áreas antes de agregar campers.")
        return

    # Solicitar el nombre del área
    nombre_area = input("Ingrese el nombre del área de entrenamiento al que desea agregar campers: ")

    # Buscar el área por nombre
    area_encontrada = None
    for area in lista_areas:
        if 'nombre_area' in area and area['nombre_area'] == nombre_area:
            area_encontrada = area
            break

    if area_encontrada is not None:
        # Mostrar la capacidad máxima y campers inscritos
        print(f"Área: {area_encontrada['nombre_area']}")
        print(f"Capacidad Máxima: {area_encontrada['capacidad_maxima']}")
        print(f"Campers Inscritos: {len(area_encontrada['campers_inscritos'])}")

        # Verificar si hay espacio disponible
        if len(area_encontrada['campers_inscritos']) < area_encontrada['capacidad_maxima']:
            # Solicitar la identificación del camper a agregar
            identificacion_camper = int(input("Ingrese la identificación del camper que desea agregar al área: "))

            # Buscar el camper por identificación
            camper_encontrado = None
            for camper in lista_campers:
                if 'identificacion' in camper and camper['identificacion'] == identificacion_camper:
                    camper_encontrado = camper
                    break

            if camper_encontrado is not None:
                # Verificar si el camper ya está inscrito en alguna área
                inscrito_en_otra_area = any(camper_encontrado['identificacion'] in area['campers_inscritos'] for area in lista_areas)
                if not inscrito_en_otra_area:
                    # Agregar el camper al área y actualizar la lista
                    area_encontrada['campers_inscritos'].append(camper_encontrado['identificacion'])
                    print(f"Camper {camper_encontrado['nombre']} {camper_encontrado['apellido']} agregado al área {nombre_area}.")
                    guardar_areas_json()
                else:
                    print("El camper ya está inscrito en otra área. No se puede agregar.")
            else:
                print("Camper no encontrado. Intente de nuevo.")
        else:
            print("El área de entrenamiento está llena. No se pueden agregar más campers.")
    else:
        print(f"No se encontró el área de entrenamiento '{nombre_area}'. Intente de nuevo.")

def registrar_area_entrenamiento():
    limpiar_pantalla()
    nombre_area = input("Ingrese el nombre del área de entrenamiento: ")
    capacidad_maxima = int(input("Ingrese la capacidad máxima del área de entrenamiento: "))

    area_entrenamiento = {
        'nombre_area': nombre_area,
        'capacidad_maxima': capacidad_maxima,
        'campers_inscritos': []
    }

    lista_areas.append(area_entrenamiento)
    print(f"Área de entrenamiento '{nombre_area}' registrada con éxito.")
    guardar_areas_json()

def listar_areas_entrenamiento():
    limpiar_pantalla()
    lista_areas = cargar_areas_json()  # Cargar las áreas actualizadas
    print("Listado de áreas de entrenamiento:")
    for area in lista_areas:
        if 'nombre_area' in area:
            print(f"Nombre: {area['nombre_area']}, Capacidad Máxima: {area['capacidad_maxima']}, Campers Inscritos: {len(area['campers_inscritos'])}")
def modificar_area():
    limpiar_pantalla()
    listar_areas_entrenamiento()

    if not lista_areas:
        print("No hay áreas de entrenamiento registradas. Registre áreas antes de modificar aulas.")
        return

    # Solicitar el nombre del área
    nombre_area = input("Ingrese el nombre del área de entrenamiento cuyo aula desea modificar: ")

    # Buscar el área por nombre
    area_encontrada = None
    for area in lista_areas:
        if 'nombre_area' in area and area['nombre_area'] == nombre_area:
            area_encontrada = area
            break

    if area_encontrada is not None:
        # Mostrar la información actual del aula
        print(f"Aula actual para el área '{nombre_area}': {area_encontrada.get('aula', 'No asignada')}")

        # Solicitar la nueva información del aula
        nueva_aula = input("Ingrese la nueva información del aula (o deje en blanco para no asignar): ").strip()

        # Actualizar la información del aula y guardar cambios
        area_encontrada['aula'] = nueva_aula
        guardar_areas_json()

        print(f"Aula modificada con éxito para el área '{nombre_area}'.")
    else:
        print(f"No se encontró el área de entrenamiento '{nombre_area}'. Intente de nuevo.")

# FUNCIONES RUTAS

def crear_ruta_entrenamiento():
    limpiar_pantalla()
    nombre_ruta = input("Ingrese el nombre de la ruta de entrenamiento: ")
    sgdb_principal = input("Ingrese el SGDB principal de la ruta: ")
    sgdb_alternativo = input("Ingrese el SGDB alternativo de la ruta: ")

    ruta_entrenamiento = {
        'nombre_ruta': nombre_ruta,
        'sgdb_principal': sgdb_principal,
        'sgdb_alternativo': sgdb_alternativo,
        'materias': ['Fundamentos de programación', 'Programación Web', 'Programación formal', 'Bases de datos', 'Backend'],
        'campers_inscritos': []
    }

    lista_rutas.append(ruta_entrenamiento)
    print(f"Ruta de entrenamiento '{nombre_ruta}' creada con éxito.")
    guardar_json_rutas()


def listar_rutas_entrenamiento():
    limpiar_pantalla()
    print("Listado de rutas de entrenamiento:")
    for ruta in lista_rutas:
        if 'nombre_ruta' in ruta:
            print(f"Nombre: {ruta['nombre_ruta']}, SGDB Principal: {ruta['sgdb_principal']}, SGDB Alternativo: {ruta['sgdb_alternativo']}, Materias: {', '.join(ruta['materias'])}")

def borrar_ruta_entrenamiento():
    limpiar_pantalla()
    nombre_ruta = input("Ingrese el nombre de la ruta de entrenamiento que desea borrar: ")

    for i, ruta in enumerate(lista_rutas):
        if 'nombre_ruta' in ruta and ruta['nombre_ruta'] == nombre_ruta:
            del lista_rutas[i]
            print(f"Ruta de entrenamiento '{nombre_ruta}' eliminada con éxito.")
            guardar_rutas_json()
            return

    print(f"No se encontró la ruta de entrenamiento '{nombre_ruta}'.")
