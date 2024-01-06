import json
import os


def guardar_campers_json():
    try:
        with open(os.path.join("base_datos", "campers.json"), 'r') as archivo_json:
            lista_campers = json.load(archivo_json)
        print("La lista de campers ha sido cargada")
        return lista_campers
    except FileNotFoundError:
        return []

def guardar_json():
    try:
        with open(os.path.join("base_datos", "campers.json"), 'w') as archivo_json:
            json.dump(lista_campers, archivo_json, indent=2)
        print("La lista de campers ha sido guardada")
    except Exception as e:
        print(f"Error al guardar el archivo: {e}")

lista_campers = guardar_campers_json()

def registrar_campers():
    nombres = input("Ingrese el nombre del camper: ")
    apellidos = input("Ingrese el apellido del camper: ")
    identificacion = int(input("Ingrese el documento del camper: "))
    direccion = input("Ingrese la direccion del camper:  ")
    acudiente = input("Ingrese el acudiente del camper: ")
    telefono_celular = input("Ingrese el numero celular del camper: ")
    telefono_fijo = input("Ingrese el numero fijo del camper: ")
    estado = input("Ingrese el estado del camper: ")

    camper = {
        'nombre': nombres,
        'apellido': apellidos,
        'identificacion': identificacion,
        'direccion': direccion,
        'acudiente': acudiente,
        'telefono_celular': telefono_celular,
        'telefono_fijo': telefono_fijo,
        'estado': estado
    }

    lista_campers.append(camper)
    print("Se creó el camper con éxito")
    guardar_json()
    return camper

def listar_campers():
    print("Listado de campers: ")
    for camper in lista_campers:
        print(camper)
def registro_resultado():
    identificacion_a_validar = int(input("Ingrese la identificacion del camper: "))
    
    camper_encontrado = None

    for camper in lista_campers:
        if camper['identificacion'] == identificacion_a_validar:
            camper_encontrado = camper
            break

    if camper_encontrado is not None:
        nota_trabajo_practico = int(input("Ingrese la nota del trabajo practico: "))
        nota_evaluacion_filtro = int(input("Ingrese la nota de la evaluacion del filtro: "))
        nota_trabajo_clase = int(input("Ingrese la nota del trabajo en clase: "))
        
        if nota_trabajo_practico > 0 and nota_evaluacion_filtro > 0 and nota_trabajo_clase > 0:
            porcentaje_60 = float(nota_trabajo_practico * 0.6)
            porcentaje_40 = float(nota_evaluacion_filtro * 0.4)
            porcentaje_10 = float(nota_trabajo_clase * 0.1)
            resultado = float(porcentaje_60 + porcentaje_40 + porcentaje_10)

            camper_encontrado['nota_final'] = resultado  
            print(f"Resultado registrado para el estudiante {camper_encontrado['nombre']} {camper_encontrado['apellido']}.")
            guardar_json()
        else:
            print("Error: Las notas deben ser mayores a 0")
    else:
        print("El estudiante no se encuentra en la base de datos. Intente de nuevo.")

