from utils.screenController import limpiar_pantalla, pausar_pantalla
from utils.corefiles import write_json, read_json

item = read_json("data/ingredientes.json")

def editar_ingrediente():
    limpiar_pantalla()
    

    
    
    
    # try:
    #     nuevo_valor = int(nuevo_valor)
    #     if not (1 <= nuevo_valor <= 5):
    #         print(" La valoración debe estar entre 1 y 5.")
    #         return
    # except ValueError:
    #     print(" Valor inválido. Se mantiene el anterior.")
    #     return
    # elif campo == "anio":
    #     try:
    #     nuevo_valor = int(nuevo_valor)
    #     if not (1900 <= nuevo_valor <= 2100):
    #         print(" El año debe ser entre 1900 y 2100.")
    #         return
    # except ValueError:
    #     print(" Año inválido. Se mantiene el anterior.")
    #     return