from base_datos.funciones_data import *
lista_rutas = guardar_rutas_json()
#Funciones de menu camperss  

def registrar_campers():
    limpiar_pantalla()
    print("Sistema de resgitro campers")

    nombres = input("Ingrese el nombre del camper: ")
    apellidos = input("Ingrese el apellido del camper: ")
    identificacion = int(input("Ingrese el documento del camper: "))
    direccion = input("Ingrese la direccion del camper:  ")
    acudiente = input("Ingrese el acudiente del camper: ")
    telefono_celular = input("Ingrese el numero celular del camper: ")
    telefono_fijo = input("Ingrese el numero fijo del camper: ")

    camper = {
        'nombre': nombres,
        'apellido': apellidos,
        'identificacion': identificacion,
        'direccion': direccion,
        'acudiente': acudiente,
        'telefono_celular': telefono_celular,
        'telefono_fijo': telefono_fijo,
        'estado': "Inscrito"
    }

    lista_campers.append(camper)
    print("Se creó el camper con éxito")
    guardar_json()
    return camper

def listar_campers():
    limpiar_pantalla()
    print("Listado de campers: ")
    for camper in lista_campers:
        print(camper)

def registro_resultado():
    limpiar_pantalla()
    print("Sistema de notas campers")

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

            camper_encontrado['prueba_incial'] = resultado 
            if resultado >= 60:
                camper_encontrado['estado']= "Aprobado"
                print("!El estudiante aprobo c:!")
            else:
                camper_encontrado['estado']= "Aprobado"
                print("!El estudiante reprobo :c!")
            print(f"Resultado registrado para el estudiante {camper_encontrado['nombre']} {camper_encontrado['apellido']}.")
            guardar_json()
        else:
            print("Error: Las notas deben ser mayores a 0")
    else:
        print("El estudiante no se encuentra en la base de datos. Intente de nuevo.")


def definicion_ruta():
    limpiar_pantalla()
    print("Sistema de rutas campers")
    identificacion_a_validar = int(input("Ingrese la identificacion del camper: "))
    camper_encontrado = None

    for camper in lista_campers:
        if camper['identificacion'] == identificacion_a_validar:
            camper_encontrado = camper
            break

    if camper_encontrado is not None:
        if camper_encontrado['prueba_inicial'] >= 60:
            limpiar_pantalla()
            op = menu_ruta()
            if op == 1:
                camper_encontrado['ruta_camper'] = "Ruta NodeJS"
                print(f"El estudiante {camper_encontrado['nombre']} {camper_encontrado['apellido']} fue asignado en la Ruta NodeJS")
            elif op == 2:
                camper_encontrado['ruta_camper'] = "Ruta Java"
                print(f"El estudiante {camper_encontrado['nombre']} {camper_encontrado['apellido']} fue asignado en la Ruta Java")
            elif op == 3:
                camper_encontrado['ruta_camper'] = "Ruta NetCore"
                print(f"El estudiante {camper_encontrado['nombre']} {camper_encontrado['apellido']} fue asignado en la Ruta NetCore")
            else:
                print("Elija un número entre (1-3)")
            guardar_json()
        else:
            print("El estudiante no ha pasado la inscripción. La nota en la prueba inicial es inferior a 60.")
    else:
        print("El estudiante no se encuentra en la base de datos. Intente de nuevo.")

def modificar_camper():
    print("Sistema de modificacion campers")
    limpiar_pantalla()
    identificacion_a_modificar = int(input("Ingrese la identificación del camper que desea modificar: "))
    camper_encontrado = None

    for i, camper in enumerate(lista_campers):
        if camper['identificacion'] == identificacion_a_modificar:
            camper_encontrado = camper
            break

    if camper_encontrado is not None:
        print("Camper encontrado. A continuación, puede realizar modificaciones:")
        # Puedes mostrar los datos actuales del camper
        print(camper_encontrado)

        # Solicitar las modificaciones
        nombres = input("Ingrese el nuevo nombre del camper (deje en blanco para mantener el actual): ")
        apellidos = input("Ingrese el nuevo apellido del camper (deje en blanco para mantener el actual): ")
        direccion = input("Ingrese la nueva dirección del camper (deje en blanco para mantener el actual): ")
        acudiente = input("Ingrese el nuevo acudiente del camper (deje en blanco para mantener el actual): ")
        telefono_celular = input("Ingrese el nuevo número celular del camper (deje en blanco para mantener el actual): ")
        telefono_fijo = input("Ingrese el nuevo número fijo del camper (deje en blanco para mantener el actual): ")
        estado = input("Ingrese el nuevo estado del camper (deje en blanco para mantener el actual): ")

        # Actualizar los datos del camper
        if nombres:
            camper_encontrado['nombre'] = nombres
        if apellidos:
            camper_encontrado['apellido'] = apellidos
        if direccion:
            camper_encontrado['direccion'] = direccion
        if acudiente:
            camper_encontrado['acudiente'] = acudiente
        if telefono_celular:
            camper_encontrado['telefono_celular'] = telefono_celular
        if telefono_fijo:
            camper_encontrado['telefono_fijo'] = telefono_fijo
        if estado:
            camper_encontrado['estado'] = estado

        print("Camper modificado con éxito.")
        guardar_json()
    else:
        print("El camper no se encuentra en la base de datos. Intente de nuevo.")

