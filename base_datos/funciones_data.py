import json
import os
from menus.menus import *

#Funciones json campers
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
# Funciones json rutas
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
# Funciones json areas

def cargar_areas_json():
    try:
        with open(os.path.join("base_datos", "aulas.json"), 'r') as archivo_json:
            lista_areas = json.load(archivo_json)
        print("La lista de rutas ha sido cargada")
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
        

