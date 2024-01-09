from base_datos.funciones_data import *
from utilidades.funciones_camper import *

def agregar_matricula():
    limpiar_pantalla()

    # Obtener datos para la matrícula
    identificacion_camper = int(input("Ingrese la identificación del camper: "))

    # Buscar el camper por identificación
    camper_encontrado = None
    for camper in lista_campers:
        if 'identificacion' in camper and camper['identificacion'] == identificacion_camper:
            camper_encontrado = camper
            break

    if camper_encontrado is not None:
        fecha_inicio = input("Ingrese la fecha de inicio (YYYY-MM-DD): ")
        fecha_finalizacion = input("Ingrese la fecha de finalización (YYYY-MM-DD): ")
        aula_entrenamiento = input("Ingrese el salón de entrenamiento asignado: ")

        # Validar fechas ingresadas
        try:
            fecha_inicio = datetime.strptime(fecha_inicio, "%Y-%m-%d").date()
            fecha_finalizacion = datetime.strptime(fecha_finalizacion, "%Y-%m-%d").date()
        except ValueError:
            print("Error en el formato de fecha. Utilice el formato YYYY-MM-DD.")
            return

        # Buscar el aula por nombre
        aula_encontrada = next((aula for aula in lista_areas if 'nombre_area' in aula and aula['nombre_area'] == aula_entrenamiento), None)

        if aula_encontrada is not None and 'director_aula' in aula_encontrada:
            director_curso = aula_encontrada['director_aula']
            print(f"Director del aula '{aula_entrenamiento}': {director_curso}")
        else:
            print(f"El aula '{aula_entrenamiento}' no tiene director asignado por ahora.")

        # Crear la matrícula
        matricula = {
            'identificacion_camper': identificacion_camper,
            'nombre_camper': f"{camper_encontrado['nombre']} {camper_encontrado['apellido']}",
            'fecha_inicio': fecha_inicio.strftime("%Y-%m-%d"),
            'fecha_finalizacion': fecha_finalizacion.strftime("%Y-%m-%d"),
            'aula_entrenamiento': aula_entrenamiento,
            'experto_encargado': director_curso if 'director_aula' in aula_encontrada else None
        }

        # Agregar la matrícula a la lista y guardar en el archivo json
        lista_matriculas.append(matricula)
        guardar_matriculas_json()

        print("Matrícula agregada exitosamente.")
    else:
        print(f"No se encontró el camper con identificación {identificacion_camper}.")

def obtener_director_aula(nombre_aula):
        # Buscar el aula por nombre
    aula_encontrada = next((aula for aula in lista_areas if 'nombre_area' in aula and aula['nombre_area'] == nombre_aula), None)

    if aula_encontrada is not None and 'director_aula' in aula_encontrada:
        return aula_encontrada['director_aula']
    else:
        return None
    
def listar_matriculas():
    limpiar_pantalla()
    print("Listado de Matrículas:")
    for matricula in lista_matriculas:
        print(f"Identificación del Camper: {matricula['identificacion_camper']}")
        print(f"Nombre del Camper: {matricula['nombre_camper']}")
        print(f"Fecha de Inicio: {matricula['fecha_inicio']}")
        print(f"Fecha de Finalización: {matricula['fecha_finalizacion']}")
        print(f"Salón de Entrenamiento Asignado: {matricula['aula_entrenamiento']}")
        print(f"Experto Encargado: {matricula['experto_encargado']}")
        print("------------------------")

def modificar_matriculas():
    limpiar_pantalla()

    # Mostrar las matrículas existentes
    print("Listado de Matrículas:")
    for i, matricula in enumerate(lista_matriculas, start=1):
        print(f"{i}. Camper: {matricula['nombre_camper']}, Aula: {matricula['aula_entrenamiento']}, "
              f"Fecha de Inicio: {matricula['fecha_inicio']}, Fecha de Finalización: {matricula['fecha_finalizacion']}")

    # Solicitar al usuario que elija una matrícula
    try:
        indice_matricula = int(input("Ingrese el número de la matrícula que desea modificar (0 para cancelar): ")) - 1
        if indice_matricula == -1:
            print("Operación cancelada.")
            return
    except ValueError:
        print("Entrada no válida. Debe ingresar un número.")
        return

    if 0 <= indice_matricula < len(lista_matriculas):
        matricula_modificar = lista_matriculas[indice_matricula]

        # Mostrar los detalles de la matrícula seleccionada
        print("\nDetalles de la Matrícula a Modificar:")
        print(f"Camper: {matricula_modificar['nombre_camper']}")
        print(f"Fecha de Inicio: {matricula_modificar['fecha_inicio']}")
        print(f"Fecha de Finalización: {matricula_modificar['fecha_finalizacion']}")
        print(f"Salón de Entrenamiento: {matricula_modificar['aula_entrenamiento']}")
        print(f"Experto Encargado: {matricula_modificar['experto_encargado']}\n")

        # Solicitar las nuevas opciones al usuario
        nombre_ruta_nueva = input("Ingrese la nueva ruta de entrenamiento asignada (deje en blanco para mantener): ")
        fecha_inicio_nueva = input("Ingrese la nueva fecha de inicio (YYYY-MM-DD) (deje en blanco para mantener): ")
        fecha_finalizacion_nueva = input("Ingrese la nueva fecha de finalización (YYYY-MM-DD) (deje en blanco para mantener): ")
        salon_entrenamiento_nuevo = input("Ingrese el nuevo salón de entrenamiento asignado (deje en blanco para mantener): ")

        # Actualizar los valores si se ingresaron nuevas opciones
        if nombre_ruta_nueva:
            matricula_modificar['ruta_entrenamiento'] = nombre_ruta_nueva
        if fecha_inicio_nueva:
            matricula_modificar['fecha_inicio'] = fecha_inicio_nueva
        if fecha_finalizacion_nueva:
            matricula_modificar['fecha_finalizacion'] = fecha_finalizacion_nueva
        if salon_entrenamiento_nuevo:
            matricula_modificar['salon_entrenamiento'] = salon_entrenamiento_nuevo

        # Guardar los cambios en el archivo json
        guardar_matriculas_json()

        print("Matrícula modificada exitosamente.")
    else:
        print("Número de matrícula no válido. Operación cancelada.")
