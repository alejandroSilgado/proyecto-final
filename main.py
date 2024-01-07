from base_datos.funciones_data import *
from utilidades.funciones import *
from utilidades.funciones_camper import *
from utilidades.funciones_rutas import *
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
        definicion_ruta()
        input("Clic cualquier teclas [continuar]: ")
    if op == 5:
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
 
def matriculas():
    limpiar_pantalla()    
    op=menu_matriculas()
#Arranque del menu aulas 

def reportes():
    limpiar_pantalla()    
    op=menu_reportes()

def trainers():
    limpiar_pantalla()    
    op=menu_trainers()
#Arranque del menu matriculas 
    
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
        matriculas()
    elif op==5:
        reportes()
    elif op==6:
        trainers()
    elif op==7:
        print("Saliendo")
        break