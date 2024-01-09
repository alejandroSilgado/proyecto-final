from base_datos.funciones_data import *
from datetime import datetime
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
    print("Sistema calificacion modulos de los campers")

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
            camper_encontrado['nota_trabajo_clase']= nota_trabajo_clase
            camper_encontrado['nota_evaluacion_filtro']= nota_evaluacion_filtro
            camper_encontrado['nota_trabajo_practico']= nota_trabajo_practico
            camper_encontrado['nota_modulos'] = resultado 
            if resultado >= 60:
                camper_encontrado['estado']= "Aprobado"
                print("!El estudiante aprobo c:!")
            else:
                camper_encontrado['estado']= "Reprobado"
                print("!El estudiante reprobo :c!")
            print(f"Resultado registrado para el estudiante {camper_encontrado['nombre']} {camper_encontrado['apellido']}.")
            guardar_json()
        else:
            print("Error: Las notas deben ser mayores a 0")
    else:
        print("El estudiante no se encuentra en la base de datos. Intente de nuevo.")

def registro_resultado_prueba_inicial():
    limpiar_pantalla()
    print("Sistema calificacion modulos de los campers")

    identificacion_a_validar = int(input("Ingrese la identificacion del camper: "))
    
    camper_encontrado = None

    for camper in lista_campers:
        if camper['identificacion'] == identificacion_a_validar:
            camper_encontrado = camper
            break

    if camper_encontrado is not None:
        nota_prueba_incial = int(input("Ingrese la nota de la prueba inicial: "))
        
        if nota_prueba_incial > 0:
            camper_encontrado['prueba_inicial'] = nota_prueba_incial 
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

            if 1 <= op <= 3:
                ruta_seleccionada = lista_rutas[op - 1]  # Indexar la lista de rutas para obtener la ruta seleccionada
                camper_encontrado['ruta_camper'] = ruta_seleccionada['nombre_ruta']

                # Verificar si el camper ya está inscrito en esa ruta
                camper_inscrito = next((camper for camper in ruta_seleccionada['campers_inscritos'] if camper['identificacion'] == identificacion_a_validar), None)
                if camper_inscrito is None:
                    # Agregar al camper a la lista de campers_inscritos de la ruta
                    ruta_seleccionada['campers_inscritos'].append({
                        'identificacion': camper_encontrado['identificacion'],
                        'nombre': f"{camper_encontrado['nombre']} {camper_encontrado['apellido']}"
                    })

                    print(f"El estudiante {camper_encontrado['nombre']} {camper_encontrado['apellido']} fue asignado en la {ruta_seleccionada['nombre_ruta']}")

                    # Guardar los cambios en el archivo rutas.json
                    guardar_rutas_json()
                else:
                    print("El estudiante ya está inscrito en esta ruta.")
            else:
                print("Elija un número entre (1-3)")
                guardar_json()
        else:
            print("El estudiante no ha pasado la inscripción. La nota en la prueba inicial es inferior a 60.")
    else:
        print("El estudiante no se encuentra en la base de datos. Intente de nuevo.")

def modificar_camper():
    print("Sistema de modificación de campers")
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

        # Nuevas variables a modificar
        nota_trabajo_clase = input("Ingrese la nueva nota del trabajo en clase (deje en blanco para mantener la actual): ")
        nota_evaluacion_filtro = input("Ingrese la nueva nota de la evaluación del filtro (deje en blanco para mantener la actual): ")
        nota_trabajo_practico = input("Ingrese la nueva nota del trabajo práctico (deje en blanco para mantener la actual): ")
        nota_modulos = input("Ingrese la nueva nota de módulos (deje en blanco para mantener la actual): ")
        prueba_inicial = input("Ingrese la nueva nota de la prueba inicial (deje en blanco para mantener la actual): ")

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
        
        # Actualizar las nuevas variables
        if nota_trabajo_clase:
            camper_encontrado['nota_trabajo_clase'] = int(nota_trabajo_clase)
        if nota_evaluacion_filtro:
            camper_encontrado['nota_evaluacion_filtro'] = int(nota_evaluacion_filtro)
        if nota_trabajo_practico:
            camper_encontrado['nota_trabajo_practico'] = int(nota_trabajo_practico)
        if nota_modulos:
            camper_encontrado['nota_modulos'] = int(nota_modulos)
        if prueba_inicial:
            camper_encontrado['prueba_inicial'] = int(prueba_inicial)

        print("Camper modificado con éxito.")
        guardar_json()
    else:
        print("El camper no se encuentra en la base de datos. Intente de nuevo.")
