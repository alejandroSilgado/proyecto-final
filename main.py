from base_datos.funciones_data import *
from utilidades.funciones import *
from utilidades.funciones_camper import *
from utilidades.funciones_rutas import *
from utilidades.funciones_trainers import *
from utilidades.funciones_matriculas import *
from utilidades.funciones_reportes import *
from menus.menus import *

#Arranque del menu campers
#FUNCIONAL

def campers():      
    limpiar_pantalla()
    op=menu_campers()
    if op==1:
        registrar_campers()
        input("Clic cualquier teclas [continuar]: ")
    if op==2:
        listar_campers()
        input("Clic cualquier teclas [continuar]: ")
    if op == 3:
        registro_resultado()
        input("Clic cualquier teclas [continuar]: ")
    if op == 4:
        registro_resultado_prueba_inicial()
        input("Clic cualquier teclas [continuar]: ")
    if op == 5:
        definicion_ruta()
        input("Clic cualquier teclas [continuar]: ")
    if op == 6:
        modificar_camper()
        input("Clic cualquier teclas [continuar]: ")

#Arranque del menu rutas 
#FUNCIONAL  
def rutas():
    limpiar_pantalla()
    op= menu_rutas()
    if op == 1:
        crear_ruta_entrenamiento()
        input("Presione Enter para continuar...")
    if op == 2:
        listar_rutas_entrenamiento()
        input("Presione Enter para continuar...")
    if op == 3:
        borrar_ruta_entrenamiento()
        input("Presione Enter para continuar...")
   
#Arranque del menu aulas 
#FUNCIONAL
def aulas():
    limpiar_pantalla()    
    op=menu_aulas()
    if op == 1:
        registrar_area_entrenamiento()
        input("Presione Enter para continuar...")
    if op == 2:
        agregar_camper_a_area()
        input("Presione Enter para continuar...")
    if op == 3:
        listar_areas_entrenamiento()
        input("Presione Enter para continuar...")
    if op == 4:
        modificar_area()
        input("Presione Enter para continuar...")

# ARRANQUE MENU DE TRAINERS

def trainers():
    limpiar_pantalla()    
    op=menu_trainers()
    if op == 1:
        crear_trainer()
        input("Presione Enter para continuar...")
    if op == 2:
        buscar_trainer()
        input("Presione Enter para continuar...")
    if op == 3:
        modificar_trainers()
        input("Presione Enter para continuar...")
    if op == 4:
        listar_trainers()
        input("Presione Enter para continuar...") 
    if op == 5:
        agregar_ruta_a_trainer_por_nombre()
        input("Presione Enter para continuar...") 
    if op == 6:
        agregar_aula_a_trainer()
        input("Presione Enter para continuar...") 

 
def matriculas():
    limpiar_pantalla()    
    op=menu_matriculas()
    if op == 1:
        agregar_matricula()
        input("Presione Enter para continuar...")
    if op == 2:
        listar_matriculas()
        input("Presione Enter para continuar...")
    if op == 3:
        modificar_matriculas()
        input("Presione Enter para continuar...")
          
# Arranque del menu aulas 

def reportes():
    limpiar_pantalla()    
    op=menu_reportes()
    if op == 1:
        listar_campers_inscritos()
        input("Presione Enter para continuar...")
    elif op == 2:
        campers_aprobados()
        input("Presione Enter para continuar...")
    elif op == 3:
        listar_trainers()
        input("Presione Enter para continuar...")
    elif op == 4:
        reprobados_aprobados_modulos()
        input("Presione Enter para continuar...")

 
#Arranque del menu principal 
while True: 
    limpiar_pantalla()
    op=menu_principal()
    if  op==1:
        campers()
    elif op==2:
        rutas()
    elif op==3:
        aulas()
    elif op==4:
        trainers()
    elif op==5:
        matriculas()
    elif op==6:
        reportes()
    elif op==7:
        print("Saliendo")
        break