import json
import os
from menus.menus import *

# FUNCIONES PARA CAMPERS

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
# FUNCIONES PARA RUTAS

def guardar_rutas_json():
    try:
        with open(os.path.join("base_datos", "rutas.json"), 'r') as archivo_json:
            lista_rutas = json.load(archivo_json)
        print("La lista de rutas ha sido cargada")
        return lista_rutas
    except FileNotFoundError:
        return []

def guardar_json_rutas():
    try:
        with open(os.path.join("base_datos", "rutas.json"), 'w') as archivo_json: 
            json.dump(lista_rutas, archivo_json, indent=2)
        print("La lista de rutas ha sido  guardada")
    except Exception as e:
        print(f"Error al guardar el archivo: {e}")

lista_rutas = guardar_rutas_json()

# FUNCIONES PARA AREAS

def cargar_areas_json():
    try:
        with open(os.path.join("base_datos", "aulas.json"), 'r') as archivo_json:
            lista_areas = json.load(archivo_json)
        print("La lista de áreas ha sido cargada")
        return lista_areas
    except FileNotFoundError:
        return []

def guardar_areas_json():
    try:
        with open(os.path.join("base_datos", "aulas.json"), 'w') as archivo_json: 
            json.dump(lista_areas, archivo_json, indent=2)
        print("La lista de áreas ha sido guardada")
    except Exception as e:
        print(f"Error al guardar el archivo: {e}")
        
lista_areas=cargar_areas_json()
        
# FUNCIONES PARA TRAINERS
def cargar_trainers_json():
    try:
        with open(os.path.join("base_datos", "trainers.json"), 'r') as archivo_json:
            lista_trainers = json.load(archivo_json)
        print("La lista de entrenadores ha sido cargada")
        return lista_trainers
    except FileNotFoundError:
        return []

def guardar_trainers_json():
    try:
        with open(os.path.join("base_datos", "trainers.json"), 'w') as archivo_json: 
            json.dump(lista_trainers, archivo_json, indent=2)
        print("La lista de entrenadores ha sido guardada")
    except Exception as e:
        print(f"Error al guardar el archivo: {e}")

lista_trainers = cargar_trainers_json()

# FUNCIONES PARA MATRICULAS
def cargar_matriculas_json():
    try:
        with open(os.path.join("base_datos", "matriculas.json"), 'r') as archivo_json:
            lista_matriculas = json.load(archivo_json)
        print("La lista de matriculas ha sido cargada")
        return lista_matriculas
    except FileNotFoundError:
        return []

def guardar_matriculas_json():
    try:
        with open(os.path.join("base_datos", "matriculas.json"), 'w') as archivo_json: 
            json.dump(lista_matriculas, archivo_json, indent=2)
        print("La lista de entrenadores ha sido guardada")
    except Exception as e:
        print(f"Error al guardar el archivo: {e}")
        
lista_matriculas = cargar_matriculas_json()

