import utils.corefiles as core
import utils.dataHandler as dataHandler
import utils.screenController as screenC
from tabulate import tabulate

def eliminar_ingrediente():
    ingredientes = core.read_json(dataHandler.ingredientes_path)
    ingrediente = input("Ingrediente a eliminar (nombre): ").strip()
    
    ingredientes = [i for i in ingredientes if i.get('nombre') != ingrediente]
    
    core.write_json(dataHandler.ingredientes_path, ingredientes)
    print(f"Ingrediente {ingrediente} eliminado con éxito.")

def eliminar_hamburguesa():
    hamburguesas = core.read_json(dataHandler.hamburguesas_path)
    hamburguesa = input("Hamburguesa a eliminar (nombre): ").strip()
    
    hamburguesas = [h for h in hamburguesas if h.get('nombre') != hamburguesa]
    
    core.write_json(dataHandler.hamburguesas_path, hamburguesas)
    print(f"Hamburguesa {hamburguesa} eliminada con éxito.")

def eliminar_categoria():
    categorias = core.read_json(dataHandler.categorias_path)
    categoria = input("Categoria a eliminar (nombre): ").strip()
    categorias = [c for c in categorias if c.get('nombre') != categoria]
    core.write_json(dataHandler.categorias_path, categorias)
    print(f"Categoría {categoria} eliminada con éxito.")

def eliminar_chef():
    chefs = core.read_json(dataHandler.chefs_path)
    chef = input("Chef a eliminar (nombre): ").strip()
    chefs = [c for c in chefs if c.get('nombre') != chef]
    core.write_json(dataHandler.chefs_path, chefs)
    print(f"Chef {chef} eliminado con éxito.")
