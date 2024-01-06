from base_datos.funciones_data import *
from utilidades.funciones import *
from menus.menus import *
#Arranque del menu campers 
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

#Arranque del menu trainers 

def trainers():
    limpiar_pantalla()    
    op=menu_trainers()
#Arranque del menu matriculas 

def matriculas():
    limpiar_pantalla()    
    op=menu_matriculas()
#Arranque del menu aulas 

def aulas():
    limpiar_pantalla()    
    op=menu_aulas()
def reportes():
    limpiar_pantalla()    
    op=menu_reportes()
#Arranque del menu principal 
while True: 
    limpiar_pantalla()
    op=menu_principal()
    if  op==1:
        campers()
    elif op==2:
        trainers()
    elif op==3:
        matriculas()
    elif op==4:
        aulas()
    elif op==5:
        reportes()
    elif op==6:
        print("Saliendo")
        break